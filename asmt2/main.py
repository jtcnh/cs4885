"""
Code Along 1
1/27/2026

Calibration from Chessboard

"""
import cv2 as cv
import numpy as np
import json


"""
Corner Calibration
"""
# Constants
SAVE_CAL_IMAGES = True
CALIBRATION_FILE = "cameraCalibration.json"
IMAGE_NAME = "calibrationImage%d.jpg"
IMAGE_PATH = "./exportedImages/"

# Variables
nValidImages = 0
rowCorners = 9
columnCorners = 6
objPtsArray = []
imgPtsArray = []
patternSize = (rowCorners, columnCorners)
key = ord("k")
webcam = cv.VideoCapture(0)
totalImagePath = str.format("%s%s", IMAGE_PATH, IMAGE_NAME)
#squareSize = 22

# refine stopping criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TermCriteria_MAX_ITER, 20, 0.001)

# create the grid of corresponding object points
objectPoints = np.zeros((rowCorners*columnCorners, 3), np.float32)
objectPoints[:,:2] = np.mgrid[0:rowCorners, 0:columnCorners].T.reshape(-1,2)

# get valid images
while (nValidImages < 10) and (key != 27):
    img = webcam.read()
    raw = img[1].copy()

    # grayscale
    gray = cv.cvtColor(raw, cv.COLOR_BGR2GRAY)

    # find chessboard pattern
    ret, corners = cv.findChessboardCorners(gray, patternSize, None)
    # print(ret)

    # if we found chesscorners
    if ret == True:
        # increase valid image count
        nValidImages += 1

        # append obj points to arr
        objPtsArray.append(objectPoints)

        # refine the corners
        corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)

        # append to imgpts array
        imgPtsArray.append(corners2)

        # draw corners to give visual feedback
        cv.drawChessboardCorners(raw, patternSize, corners2, ret)

        # save this calibration image to file
        if (SAVE_CAL_IMAGES == True):
            imgPath = str.format(totalImagePath, nValidImages)
            cv.imwrite(imgPath, raw)

        # show image
        cv.imshow("Image", raw)
        key = cv.waitKey(50)
    else:
        cv.imshow("Image", raw)
        key = cv.waitKey(10)


# Save calibration to file
ret, iMtx, distort, rotate, translate = cv.calibrateCamera(objPtsArray, imgPtsArray, gray.shape[::-1], None, None)
with open(CALIBRATION_FILE) as calibrationFilePtr:
    json.dump({
        "Float" : ret,
        "IntrinsicMatrix" : iMtx,
        "Distortion" : distort,
        "Rotation" : rotate,
        "Translate" : translate
    }, calibrationFilePtr)