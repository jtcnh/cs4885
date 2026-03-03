# Image Contours

import cv2 as cv
import numpy as np

def nothing(x):
    pass

key = ord('r')
webcam = cv.VideoCapture(0)


def contours():
    key = ord('r')
    cv.namedWindow('controls')
    cv.createTrackbar('lower', 'controls', 0, 255, nothing)
    cv.createTrackbar('upper', 'controls', 0, 255, nothing)
    cv.setTrackbarPos('lower', 'controls', 43)
    cv.setTrackbarPos('upper', 'controls', 127)

    while key != ord('s'):
        still = webcam.read()
        og_img = still[1].copy()
        img = cv.cvtColor(still[1], cv.COLOR_BGR2GRAY)
        img = cv.GaussianBlur(img, (7,7), 0)

        lower = int(cv.getTrackbarPos('lower', 'controls'))
        upper = int(cv.getTrackbarPos('upper', 'controls'))


        # Edges detection
        img = cv.Canny(img, lower, upper)
        contours, heirarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        contours = list(contours)
        contours.sort(key=cv.contourArea, reverse=True)
        contours = contours[0]


        # Draw Contours
        cv.drawContours(og_img, contours, -1, (255, 0,0), 3)
        img = og_img


        # bounding rect
        x,y,w,h = cv.boundingRect(contours)
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

        cv.imshow('Image', img)
        key = cv.waitKey(5)

contours()
    