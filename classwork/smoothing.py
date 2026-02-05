import cv2 as cv
import numpy as np

from mvutil import showImage

import cvlib

img = cv.imread('../images/octopus.jpg')


# Simple / Average Box Blur
def simpleBlur(img, blurSize=1):
    return cv.blur(img, (blurSize,blurSize))


# Gaussian Blur
def gaussianBlur(img, blurSize=1):
    return cv.GaussianBlur(img, (blurSize,blurSize), 0)


# Median Blur
def medianBlur(img, blurSize=1):
    return cv.medianBlur(img, blurSize)

showImage(medianBlur(img, 15))