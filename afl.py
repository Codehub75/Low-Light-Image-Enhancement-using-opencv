import cv2
import numpy as np


img1 = cv2.imread('final.jpg')


gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)


thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2.5)



cv2.imshow('real',thresh)
cv2.imshow('kf',img1)
cv2.waitKey(0)

cv2.destroyAllWindows()