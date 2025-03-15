# Seam Carving Image Resizing

This project implements the seam carving algorithm for content-aware image resizing. Unlike traditional resizing methods that uniformly scale the entire image, seam carving intelligently removes the least important pixels while preserving the important visual content.

## Overview

Seam carving works by:
1. Calculating an energy map that identifies important areas of the image
2. Finding "seams" (connected paths of pixels) with the lowest total energy
3. Removing these seams to reduce the image dimensions
4. Repeating until the desired size is reached

This implementation features:
- High-performance optimization using Numba JIT compilation
- Forward energy calculation for better quality when removing multiple seams
- Batch processing for improved efficiency
- Support for both horizontal and vertical resizing
- Visualization of removed seams

## Requirements

- Python 3.6+
- NumPy
- Pillow (PIL)
- Matplotlib
- Numba

In Google Colab, install the required packages with:
```python
!pip install numba
```

## Usage

1. Run the script in Google Colab or your local Python environment
2. Upload an image when prompted
3. Choose whether to resize by percentage or specific pixel dimensions
4. The script will process the image and display:
   - The original image
   - The resized image
   - A visualization of the removed seams
5. The results will be saved and downloadable (in Google Colab)

## Performance

This implementation includes several optimizations:

- **Numba acceleration**: Core functions are compiled to machine code for faster execution
- **Forward energy**: Uses an improved energy calculation method that produces better results for multiple seam removals
- **Efficient seam removal**: Specialized functions for removing seams with minimal overhead
- **Batch processing**: Processes seams in groups to reduce overhead

## Algorithm Details

### Energy Calculation
The implementation uses the energy function e₁ = |∂/∂x I| + |∂/∂y I| as specified in the requirements, calculating the gradient magnitude in both x and y directions.

### Forward Energy
In addition to the basic energy calculation, this implementation uses forward energy, which considers the impact of removing a pixel on its neighbors. This produces better results when removing multiple seams.

### Seam Finding
The algorithm uses dynamic programming to find the optimal seam with the lowest cumulative energy.

## Example Results

When running the script, you'll see three images:
1. **Original Image**: The input image before processing
2. **Resized Image**: The result after seam carving
3. **Seams Visualization**: Shows which seams were removed (highlighted in red)

## Performance Metrics

The script provides performance metrics including:
- Total processing time
- Number of pixels removed
- Processing speed (pixels per second)

## Notes

- The algorithm works best on images where there are clear foreground and background elements
- Images with uniform content throughout may not show dramatic improvements over traditional resizing
- Processing time increases with image size and the number of seams to be removed
- The maximum recommended image size is 800x800 pixels as specified in the requirements
- The algorithm can reduce an image's size to half its original dimensions or more

## Implementation Details

This implementation follows the project requirements:
1. Uses the specified energy calculation method
2. Implements the energy calculation from scratch without predefined functions
3. Handles images up to 800x800 pixels
4. Can reduce images to half their original size
5. Generates both the resized image and a visualization of removed seams
6. Includes significant performance optimizations for the bonus requirement
