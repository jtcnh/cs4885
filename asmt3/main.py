# Jack Chambers
# Assignment 3
# Motion Detector
# 3/5/2026


import cv2 as cv
import numpy as np


"""
Process:
[x] get webcam image
[x] grayscale image
[x] background subtraction
[ ] thresholding?
[ ] foreground / contour detection
[ ] add boxes to base image
"""

# globals
bgsub = cv.createBackgroundSubtractorMOG2()
webcam = cv.VideoCapture(0)
key = ord('r')

## videoframe loop
# breaks when 'ESC' key is pressed (27)
while (key != 27):
    # get webcam image
    img_raw = webcam.read()[1]
    img = img_raw.copy()

    ## grayscale webcam image
    grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #grayscale = cv.convertScaleAbs(grayscale, alpha=0.25, beta=1)
    #grayscale = cv.GaussianBlur(grayscale, (21, 21), 0)

    ## background subtraction
    # refrence: https://docs.opencv.org/3.4/d8/d38/tutorial_bgsegm_bg_subtraction.html
    foreground = bgsub.apply(img)

    ## create a mask of foreground regions
    # threshold background 
    ret, threshMask = cv.threshold(foreground, 127, 255, cv.THRESH_BINARY)

    # TEMP
    # reference for erosion / dilation
    # https://medium.com/@siromermer/detecting-and-tracking-moving-objects-with-background-subtractors-using-opencv-f2ff7f94586f
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
    #cv.MORPH_OPEN
    erodedMask = cv.dilate(threshMask, kernel, iterations=2)

    ## locate contours
    # reference: https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
    contours, heirarchy = cv.findContours(erodedMask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    ## filter out tiny contours
    contourSizeFilter = 2500
    drawnContours = [cnt for cnt in contours if cv.contourArea(cnt) > contourSizeFilter]

    ## draw contours on base image (B,G,R)
    #cv.drawContours(img_raw, drawnContours, -1, (0,255,0), 3)

    ## draw bounding boxes on motion objects
    output = img_raw.copy()
    for contour in drawnContours:
        x,y,w,h = cv.boundingRect(contour)
        output = cv.rectangle(output, (x,y), (x+w, y+h), (0,255,0), 3)


    ## display raw image with bounding boxes
    cv.imshow('image', output)
    cv.imshow('other', erodedMask)
    key = cv.waitKey(1)


# cleanup opencv
webcam.release()
cv.destroyAllWindows()