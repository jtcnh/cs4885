"""
Geometric Transformations
"""
import numpy as np
import cv2 as cv


octopus = cv.imread("../images/octopus.jpg")

# Image Display
def show_img(img, frames=-.10, window="Image"):
    key = ord('r')
    if frames < 0:
        while key != 27:
            cv.imshow(window, img)
            key = cv.waitKey(10)
    else:
        cv.imshow(window, img)
        key = cv.waitKey(frames)


# Image Translation
img = cv.imread("../images/boat.jpg")
row, col, channel = img.shape
# M = np.float32([
#     [1, 0, 100], 
#     [0, 1, 50]
# ])
# cv.warpAffine(img, M, (col, row))
# show_img(img)


# Image Rotation
M = cv.getRotationMatrix2D(((col-1)/2.0, (row-1)/2.0), 180, 1)
img = cv.warpAffine(img, M, (col, row))
show_img(img)