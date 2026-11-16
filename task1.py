import numpy as np
import cv2
img = cv2.imread('download.jpg',1)
while True:
       
        cv2.imshow('Rotatable Image', img)
         
        key = cv2.waitKey(1) & 0xFF
         
        if key == ord('r'):
            
            img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            print("Image rotated 90 degrees clockwise.")
        

        elif key == ord('q'):
         break
   