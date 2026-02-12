"""
Geometric Transformations

Transformations:
    Affine
    Perspective
    Color
    Brightness
    Contrast
    Gamma Correction

"""
import numpy as np
import cv2 as cv


octopus = cv.imread("../images/octopus.jpg")
img = cv.imread("../images/boat.jpg")


# Image Translation
def translate(img, offset=(0,0)):
    row, col = img.shape
    M = np.float32([
        [1, 0, offset[0]], 
        [0, 1, offset[1]]
    ])
    return cv.warpAffine(img, M, (col, row))


# Image Rotation
def getCenter(img):
    row, col = img.shape
    return ((col-1)/2.0, (row-1)/2.0)


# Rotate an image using degrees
def rotate(img, rotation=0):
    row, col = img.shape
    center = getCenter(img)
    M = cv.getRotationMatrix2D(center, rotation, 1)
    return cv.warpAffine(img, M, (col, row))


# Rotate an image using a rotation matrix
def rotateMatrix(img, M):
    row, col = img.shape
    return cv.warpAffine(img, M, (col, row))


# Scaling
def scaleImage(img, scalar=1):
    # cv uses row,col
    row_dim = int(img.shape[1]*scalar)
    col_dim = int(img.shape[0]*scalar)
    dim_size = (row_dim, col_dim)
    return cv.resize(img, dim_size, interpolation=cv.INTER_NEAREST)


# Color Channels
# b,g,r = cv.split(img)
# new_img = cv.merge([b,g,r])
## Using numpy
# img[:,:,2] = 0
# showImage(img)


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
