# **Object Detection using SIFT Features**

This notebook demonstrates **object detection** using **SIFT (Scale-Invariant Feature Transform)** features with **OpenCV** in **Google Colab**.

## **Basic Task: Image Matching**

The main task involves detecting a **query image** within a **target image** by:
- Extracting SIFT features (keypoints and descriptors).
- Matching features using a brute-force matcher and filtering with a ratio test.
- Drawing circles around the detected points in the target image.

### Example:
  <img src="before.png" width="45%" /> &emsp;&emsp;&emsp; <img src="after.png" width="45%" />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**Before** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; **After**


## **Bonus Task: Video Object Detection**

The bonus task extends this to video:
- SIFT features are extracted from the query image and each video frame.
- Matches are found using the ratio test.
- A **bounding box** is drawn around the detected object in each frame, and an **output video** is created.

### Example Video:
- The processed video with bounding boxes is available here:

![output_video](https://github.com/user-attachments/assets/bad85db0-9783-4f8b-939e-ac8c4278301f)



## **Usage**

1. Upload the query image (`query.jpg`), target image (`target.jpg`), query image for the bonus task (`bonus/q.jpg`), and video (`bonus/video.mp4`) to Colab.
2. Run the notebook to see the results:
   - For the basic task, detected keypoints will be shown.
   - For the bonus task, an **output video** (`output_video.mp4`) will be downloaded.

## **Customization**

- **Threshold for Ratio Test** (default 0.75) and **minimum matches** (default 10) can be adjusted.
- Video codec and format can be modified in `cv2.VideoWriter`.
