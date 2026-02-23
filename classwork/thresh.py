# thresholding
# 2/19/2026

import cv2 as cv
import numpy as np
import cvlib

img = cv.imread('../images/octopus.jpg')

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# simple thresholding: binary, truncated
# arguments = threshold followed by max value
# ret, img = cv.threshold(img, 50, 255, cv.THRESH_TRUNC)

# adaptive thresholding
img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

cvlib.show(img)