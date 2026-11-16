
# cv2.imshow('Original Image', image)
# cv2.waitKey(0)


# img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Gray Scale Image', img_gray)
# cv2.waitKey(0)


# ret, img_thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
# # display the image
# cv2.imshow('Binary Image', img_thresh)
# cv2.waitKey(0)

# # detect contours on binary image
# contours, _ = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# # draw contours on original image
# img_copy = image.copy()
# cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2, lineType=cv2.LINE_AA)

# # display the image
# cv2.imshow('Contour Image', img_copy)



import cv2
import numpy as np
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.namedWindow("LiveVideo")
cv2.namedWindow("frame")
while(True):
  
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)









    
    cv2.imshow('Binary Image', thresh)
    cv2.imshow('frame', frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.imshow('Binary Image', thresh)
cv2.imshow('frame', frame)

cap.release()


