import cv2
import numpy as np

img = cv2.imread('20200627_102116_mfnr.jpg')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.namedWindow('image1',cv2.WINDOW_NORMAL)
cv2.namedWindow('image2',cv2.WINDOW_NORMAL)
cv2.namedWindow('image3',cv2.WINDOW_NORMAL)

im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Filters (Just check the effects for now I'll make separate func for each of the filters if this one's appropriate)
im_color = cv2.applyColorMap(im_gray,cv2.COLORMAP_HSV)
im_color1 = cv2.applyColorMap(im_gray,cv2.COLORMAP_OCEAN)
im_color2 = cv2.applyColorMap(im_gray,cv2.COLORMAP_BONE)
im_color3 = cv2.applyColorMap(im_gray,cv2.COLORMAP_PLASMA)

cv2.imshow('image',im_color)
cv2.imshow('image1',im_color1)
cv2.imshow('image2',im_color2)
cv2.imshow('image3',im_color3)
cv2.waitKey(0) 
