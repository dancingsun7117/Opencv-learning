import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

while True:
    ret, frame = cap.read()


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Correct HSV range (example range, adjust for your color)
    lowerred = np.array([0, 50, 50])
    upperred = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lowerred, upperred)
    res = cv2.bitwise_and(frame, frame, mask=mask)



    cv2.imshow('Original', frame)
    cv2.imshow('2rr', mask)
    

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()