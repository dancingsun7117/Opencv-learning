import numpy as np
import cv2

img = cv2.imread('download.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(0,255,255),10)
cv2.circle(img,(100,63), 55, (255,255,0), 5)
pts = np.array([[100,100],[50,70],[125,212],[90,60]], np.int32)
cv2.polylines(img,[pts],True,(35,45,55),5)
cv2.putText(img,'hehehe',[5,100],cv2.FONT_HERSHEY_TRIPLEX,1.5,(230,76,200),2,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()