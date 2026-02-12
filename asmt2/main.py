"""
Jack Chambers
Assignment 2
2/12/2026
"""

import cv2 as cv
import cvlib
import cvcalibration as cvcal

CAL_FILE = "./camera_calibration.json"
RAW_IMG_FILE = "./raw_checker.jpg"

# create and save calibration
thisCal = cvcal.CreateCalibration()
# cvcal.SaveCalibration(CAL_FILE, thisCal)

# load calibration and undistort
# savedCal = cvcal.LoadCalibration(CAL_FILE)
rawImg = cv.imread(RAW_IMG_FILE)
outputImg = cvcal.Undistort(rawImg, thisCal)

# display output image
cvlib.show(outputImg)