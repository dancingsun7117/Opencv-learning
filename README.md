# OpenCV Learning Exercises

Practice scripts from learning OpenCV. These are tutorial-style exercises, not a finished project.

## Topics covered
- Reading, showing and saving images and video (`video1`-`video6`, `task1`)
- Webcam capture, rotation and an FPS overlay (`task1.5`, `task2`)
- Mouse callbacks to read pixel coordinates and colours (`task3`)
- HSV colour masking with a mouse-picked colour (`task4`, `video7`-`video10`)
- Morphology: erosion, dilation, opening, closing (`video9`)
- Edge and gradient filters: Canny, Sobel, Laplacian (`video10`)
- Template matching, foreground extraction, corner detection, feature matching (`video11`-`video14`)
- Background subtraction with MOG2 (`video15`)
- Haar-cascade face and eye detection (`video16`)

## How to run
```
pip install -r requirements.txt
python video10.py
```
Several scripts open a webcam; change `cv2.VideoCapture(0)` to your camera index if needed.
