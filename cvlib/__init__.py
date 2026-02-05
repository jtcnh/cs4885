"""
Jack Chambers
CV utility methods libary 'cvlib'
2/5/2026
"""

import cv2 as cv
import numpy as np


# Image Translation
def translate(img, offset=(0,0)):
    row, col = img.shape
    M = np.float32([
        [1, 0, offset[0]], 
        [0, 1, offset[1]]
    ])
    return cv.warpAffine(img, M, (col, row))


# Get Image Center
def getCenter(img):
    row, col = img.shape
    return ((col-1)/2.0, (row-1)/2.0)


# Image Rotation
def rotate(img, rotation=0):
    row, col = img.shape
    center = getCenter(img)
    M = cv.getRotationMatrix2D(center, 180, 1)
    return cv.warpAffine(img, M, (col, row))


# Scaling
def scaleImage(img, scalar=1):
    # cv uses row,col
    row_dim = int(img.shape[1]*scalar)
    col_dim = int(img.shape[0]*scalar)
    dim_size = (row_dim, col_dim)
    return cv.resize(img, dim_size, interpolation=cv.INTER_NEAREST)


# Brightness / Contrast
"""
f = img
a = contrast (multiply)
b = brightness (additive)
g = newImg
g = af+b
"""
def contrastBrightness(img, contrast=1, brightness=1):
    return cv.convertScaleAbs(img, alpha=contrast, beta=brightness)


# Gamma
"""
p = (I/255)^gamma - 255
"""
def gamma(img, gamma=1):
    # generate a LUT to save on the exp calculations
    lut = np.empty((1, 256), np.uint8)
    for i in range(256):
        lut[0][i] = np.clip(pow(i/255.0, gamma)*255.0, 0, 255)

    return cv.LUT(img, lut)


# Draw text
def text(img, text, 
        org=(100,225), 
        font=cv.FONT_HERSHEY_SIMPLEX, 
        fontScale=1, 
        color=(255,255,255), 
        thickness=2,
        lineType = cv.LINE_AA
    ):
    
    newImg = img.copy() # images are pass by reference, not copies
    cv.putText(newImg, text, org, font, fontScale, color, thickness, lineType)
    return newImg


# Simple / Average Box Blur
def simpleBlur(img, blurSize=1):
    return cv.blur(img, (blurSize,blurSize))


# Gaussian Blur
def gaussianBlur(img, blurSize=1):
    return cv.GaussianBlur(img, (blurSize,blurSize), 0)


# Median Blur
def medianBlur(img, blurSize=1):
    return cv.medianBlur(img, blurSize)