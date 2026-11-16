import cv2
import numpy as np

img = cv2.imread('Screenshot.png')

img1 = cv2.resize(img,(500,500),interpolation= cv2.INTER_LINEAR)
retval, threshold = cv2.threshold(img1, 170,200, cv2.THRESH_BINARY)
grayscaled = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
retval12,threshold2 = cv2.threshold(grayscaled, 170, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 115, 1)
retval2,threshold3 = cv2.threshold(grayscaled,160,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('Adaptive threshold',gaus)
cv2.imshow('og',img1)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('threshold3',threshold3)
cv2.waitKey(0)
cv2.destroyAllWindows()