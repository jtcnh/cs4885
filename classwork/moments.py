# Image Moments
# 3/3/2026

import cv2 as cv
import numpy as np
import json

def moments(img_name):
    key = ord('r')
    still = cv.imread(img_name, cv.IMREAD_GRAYSCALE)
    still = cv.resize(still, (0,0), fx=0.1, fy=0.1)
    og_img = still.copy()
    img = still


    # gaussian blur
    img = cv.GaussianBlur(img, (7,7), 0)
    lower = 66
    upper = 185

    img = cv.Canny(img, lower, upper)
    contours, heirachy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


    # get the biggest contour
    areas = [cv.contourArea(c) for c in contours]
    max_area = np.argmax(areas)
    single_contour = contours[max_area]


    # get the moments
    moments = cv.moments(single_contour)
    print(json.dumps(moments, indent=4))
    center_pt_x = int(moments['m10']/moments['m00'])
    center_pt_y = int(moments['m01']/moments['m00'])


    # draw contours
    cv.drawContours(og_img, [single_contour], -1, (255,0,0), 3)
    cv.circle(og_img, [center_pt_x, center_pt_y], 2, (255, 255,255), -1)
    img = og_img

    cv.imshow("Image", img)
    key = cv.waitKey(0)

moments("./images/ponytail_1.jpg")