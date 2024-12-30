# Face Detection with OpenCV

This program uses OpenCV's Haar Cascade Classifier to detect faces in a set of images. It processes each image in the 'images' directory, detects faces, and saves the images with drawn bounding boxes around detected faces to a new directory called 'face-images'.

## Features

- **Face Detection**: Detects faces in images using the Haar Cascade Classifier.
- **Image Processing**: Processes images in grayscale for better detection accuracy.
- **Bounding Boxes**: Draws rectangles around detected faces.
- **Saving Results**: Saves the images with faces marked in the 'face-images' folder if more than one face is detected.
  
## Requirements

- Python 3.x
- OpenCV (`cv2` module)
- Haar Cascade XML file for frontal face detection (`haarcascade_frontalface_default.xml`)

