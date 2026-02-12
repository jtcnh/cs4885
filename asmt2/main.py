"""
Jack Chambers
Assignment 2
2/12/2026
"""

import cvlib
from Calibration import *

CAL_FILE = "./camera_calibration.json"
RAW_IMG = "./selfie.jpg"

# create and save calibration
thisCal = CreateCalibration()
SaveCalibration(CAL_FILE, thisCal)

# load calibration and undistort
savedCal = LoadCalibration(CAL_FILE)
outputImg = Undistort(RAW_IMG, savedCal)

# display output image
cvlib.show(outputImg)