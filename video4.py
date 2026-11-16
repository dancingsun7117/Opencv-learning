import cv2
import numpy as np

img = cv2.imread('download.jpg',cv2.IMREAD_COLOR)

img[55,55] = [0,255,255]
px = img[55,55] 
img[100:150,100:150] = [0,255,255]
face = img[60:100,60:100]
img[0:40,0:40] = face
print(px)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()