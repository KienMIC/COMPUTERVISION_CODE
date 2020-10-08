# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 22:57:09 2020

@author: KIENMIC
"""

import numpy
import cv2
import os
import sys
from glob import glob
img_mask = "F:/PICTURE/*.jpg"
img_names = glob(img_mask)
for img_path in img_names:
    img = cv2.imread(img_path)
    print(img_path)
    cv2.imshow("Input Image",img)
    if(cv2.waitKey(1000) == 27):
        break