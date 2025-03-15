import sys
import numpy as np
from imageio import imread, imwrite
from tqdm import trange

def calc_energy(img):
    
    img = img.astype(np.float32)

    dx = np.zeros_like(img)
    dy = np.zeros_like(img)

   
    dx[:, 1:-1] = img[:, 2:] - img[:, :-2]  
    dy[1:-1, :] = img[2:, :] - img[:-2, :]  

    energy_map = np.abs(dx) + np.abs(dy)
    return energy_map.sum(axis=2) 

def minimum_seam(img):
   
    r, c, _ = img.shape
    energy_map = calc_energy(img)

    M = energy_map.copy()
    backtrack = np.zeros_like(M, dtype=np.int32)

    for i in range(1, r):
        for j in range(c):
            left = M[i-1, j-1] if j > 0 else float('inf')
            up = M[i-1, j]
            right = M[i-1, j+1] if j < c-1 else float('inf')

            min_energy = min(left, up, right)

            if min_energy == left:
                backtrack[i, j] = j - 1
            elif min_energy == right:
                backtrack[i, j] = j + 1
            else:
                backtrack[i, j] = j

            M[i, j] += min_energy

    return M, backtrack

def carve_column(img, seam_tracker):
    """Removes the lowest-energy vertical seam and tracks removed seams."""
    r, c, _ = img.shape
    M, backtrack = minimum_seam(img)

    mask = np.ones((r, c), dtype=np.bool_)
    j = np.argmin(M[-1])

    seam = []  # Store removed seam coordinates
    for i in reversed(range(r)):
        mask[i, j] = False
        seam.append((i, j, 'v'))  # Track seam with 'v' for vertical
        j = backtrack[i, j]

    mask = np.stack([mask] * 3, axis=2)
    img = img[mask].reshape((r, c - 1, 3))

    seam_tracker.append(seam)  # Save removed seam
    return img

def crop_c(img, scale_c):
    """Reduces the width of the image while tracking removed seams."""
    r, c, _ = img.shape
    new_c = int(scale_c * c)

    seam_tracker = []
    for _ in trange(c - new_c, desc="Removing Vertical Seams"):
        img = carve_column(img, seam_tracker)

    return img, seam_tracker

def crop_r(img, scale_r):
    """Reduces the height of the image while tracking removed seams."""
    img = np.rot90(img, 1, (0, 1))  # Rotate to treat rows as columns
    img, seam_tracker = crop_c(img, scale_r)  # Remove rows as columns
    img = np.rot90(img, 3, (0, 1))  # Rotate back

   
    adjusted_seams = []
    for seam in seam_tracker:
        new_seam = [(y, x, 'h') for x, y, _ in seam]  
        adjusted_seams.append(new_seam)

    return img, adjusted_seams

def crop_both(img, scale):
    
    img, seams_c = crop_c(img, scale)
    original_width = img.shape[1]  

    
    img, seams_r = crop_r(img, scale)

    
    for seam in seams_r:
        for i, (x, y, direction) in enumerate(seam):
           
            seam[i] = (x, min(y, original_width - 1), direction)

    return img, seams_c + seams_r

def visualize_seams(img, seams):
    
    img_with_seams = img.copy()
    for seam in seams:
        for i, j, direction in seam:
            if direction == 'v':
                img_with_seams[i, j] = [255, 0, 0] 
            else:
                img_with_seams[i, j] = [0, 0, 255]  
    return img_with_seams

def main():
    if len(sys.argv) != 5:
        print('usage: file.py <r/c/b> <scale> <image_in> <image_out>', file=sys.stderr)
        sys.exit(1)

    which_axis = sys.argv[1]
    scale = float(sys.argv[2])
    in_filename = sys.argv[3]
    out_filename = sys.argv[4]

    img = imread(in_filename)

   
    if len(img.shape) == 2:
        img = np.stack([img] * 3, axis=2)

    if which_axis == 'r':
        out, seams = crop_r(img, scale)
    elif which_axis == 'c':
        out, seams = crop_c(img, scale)
    elif which_axis == 'b':
        out, seams = crop_both(img, scale)
    else:
        print('usage: file.py <r/c/b> <scale> <image_in> <image_out>', file=sys.stderr)
        sys.exit(1)

    
    imwrite(out_filename, out)

   
    img_seams = visualize_seams(img, seams)
    seam_filename = out_filename.replace('.jpg', '_seams.jpg')
    imwrite(seam_filename, img_seams)

if __name__ == '__main__':
    main()
