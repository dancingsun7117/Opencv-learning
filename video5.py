import cv2
import numpy as np
img1 = cv2.imread('mainsvmimage.png')
img11 = cv2.resize(img1,(500,500),interpolation= cv2.INTER_LINEAR)
img2 =cv2.imread('im2.png')
img22 = cv2.resize(img2,(500,500),interpolation= cv2.INTER_LINEAR)
img3 = cv2.imread('download(3).jpg')
img33 = cv2.resize(img3,(300,300),interpolation= cv2.INTER_LINEAR)
add = img11 + img22 
add1 = cv2.add(img11,img22)
weighted = cv2.addWeighted(img11,0.5,img22,0.5,0)
rows,cols,channels = img33.shape
roi = add1[0:rows,0:cols]
img2gray = cv2.cvtColor(img33,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)
add1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
img33_fg = cv2.bitwise_and(img33,img33,mask = mask)
dst = cv2.add(add1_bg,img33_fg)
add1[0:rows, 0:cols ] = dst




cv2.imshow('res',add1)


cv2.imshow('add1',add1)

cv2.imshow('weighted',weighted)
cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()