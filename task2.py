import numpy as np
import cv2
import time
import math
cam = cv2.VideoCapture(0)
while True:
 start = time.time()
 ret, frame = cam.read()
 end = time.time()
 fps = math.ceil(1 / (end - start))
 cv2.putText(frame, "FPS: " + str(fps), (30, 30), cv2.FONT_ITALIC, 1, (255, 255, ),2)
 cv2.imshow("frame", frame)
 if cv2.waitKey(1000) & 0xFF == ord('q'):
  break



