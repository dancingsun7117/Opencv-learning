import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
   ret,frame = cap.read()
   # if not ret:
   #    print("Frame not found")
   #    break
   #  else:
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   lowerred = np.array([50,50,50])
   upperred = np.array([255,255,150])
   mask = cv2.inRange(hsv,lowerred,upperred)
   res = cv2.bitwise_and(frame,frame,mask=mask)
   kernel = np.ones((15,15),np.float32)/255
   smoothed = cv2.filter2D(res,-1,kernel)
   cv2.imshow('Original',frame)
   cv2.imshow('Averaging',smoothed)
  
   if cv2.waitKey(1) & 0xFF == 27:  # ESC key
      break
   

cv2.destroyAllWindows()
cap.release()