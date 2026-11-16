import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cv2.namedWindow("LiveVideo")
cv2.namedWindow("frame")
selected_hsv = None



def mouse_callback(event, x, y, flags, param):
    global selected_hsv, frame
    if event == cv2.EVENT_LBUTTONDOWN :
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        selected_hsv = hsv_frame[y, x]
        print("Selected HSV:", selected_hsv)
cv2.setMouseCallback("frame", mouse_callback)

    

while True:
    ret, frame = cap.read()
   
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
    if selected_hsv is not None:
        h, s, v = selected_hsv

        lower = np.array([h-10 , s-60 , v-60 ])
        upper = np.array([h + 10, s + 40, v + 40])

        mask = cv2.inRange(hsv_frame, lower, upper)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        # bilateral = cv2.bilateralFilter
        cv2.imshow("LiveVideo", result)
    cv2.imshow('frame', frame)
   
  

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
