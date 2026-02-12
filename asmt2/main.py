"""
Jack Chambers
Assignment 2
2/12/2026
"""

import cvlib
import cvcalibration as cvcal

CAL_FILE = "./camera_calibration.json"
RAW_IMG = "./selfie.jpg"

# create and save calibration
thisCal = cvcal.CreateCalibration()
cvcal.SaveCalibration(CAL_FILE, thisCal)

# load calibration and undistort
savedCal = cvcal.LoadCalibration(CAL_FILE)
outputImg = cvcal.Undistort(RAW_IMG, savedCal)

# display output image
cvlib.show(outputImg)