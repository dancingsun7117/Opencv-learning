import cv2
import numpy as np
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) 



while (True):
 global frame  
 ret, frame = cap.read()
 cv2.imshow('frame', frame)
 key = cv2.waitKey(1) & 0xFF
        
 if key == ord('r'):
        
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)  
        cv2.imshow('frame', frame)
        cv2.waitKey(1) & 0xFF

        print("video rotated 90 degrees clockwise.")
 elif key == ord('q'):
  break


cap.release()

