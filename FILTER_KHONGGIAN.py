# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 21:22:56 2020

@author: KIENMIC
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("A.jpg")
img_gauss = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
img_medium = cv2.medianBlur(img,5)
img_bilateral = cv2.bilateralFilter(img,9,75,75)


kernel = np.array([[0, -1, 0], 
                   [-1, 5,-1], 
                   [0, -1, 0]])

image_sharp = cv2.filter2D(img, -1, kernel)

img_AnhGop = np.hstack((img,image_sharp))


cv2.imshow("Original Image",img)
cv2.imshow("Gaussian Image",img_gauss)
cv2.imshow("Medium Image",img_medium)
cv2.imshow("Bilateral Image",img_bilateral)
cv2.imshow('Linear Sharp Image',img_AnhGop)
cv2.waitKey(0)
cv2.destroyAllWindows()