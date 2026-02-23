# trackbars.py
import cv2 as cv
import numpy as np

webcam = cv.VideoCapture(0)

def nothing(x):
    pass

def threshold():
    key = ord('r')
    cv.namedWindow('controls')
    cv.createTrackbar('threshold', 'controls', 0, 255, nothing)
    cv.setTrackbarPos('threshold', 'controls', 127)

    while key != 27:
        still = webcam.read()
        
        # convert still to grayscale
        img = cv.cvtColor(still[1], cv.COLOR_BGR2GRAY)

        # gaussian blur
        img = cv.GaussianBlur(img, (7,7), 0)
        thresh = int(cv.getTrackbarPos('threshold', 'controls'))
        ret, img = cv.threshold(img, thresh, 255, cv.THRESH_BINARY)

        cv.imshow('Image', img)
        key = cv.waitKey(5)

threshold()