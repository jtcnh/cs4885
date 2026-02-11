"""
Calibration w/ Extrinsic Matrix
"""
import cv2 as cv
import numpy as np
import json

actual_points = [
    [40,40,0],
    [160,40,0],
    [40,160,0],
    [160,160,0]
]


"""
Load Saved Materials
"""
with open("cameraCalibration.json", "r") as calFilePtr:
    loadFile = json.load(calFilePtr)

distCoeffs = np.zeros((4,1))
objectPts = np.array(actual_points).astype(np.float32)
#print(objectPts)

imgPoints = np.array(loadFile["image_points"]).astype(np.float32)
#print(imgPoints)

i_matrix = np.array(loadFile["intrinsic_matrix"]).astype(np.float32)
#print(i_matrix)
#print(i_matrix.shape)

#distCoeffs = np.array(loadFile["dist_coefs"]).astype(np.float32)

success, rvec, tvec = cv.solvePnP(objectPts, imgPoints, i_matrix, distCoeffs)

if success == True:
    rotationMatrix, _ = cv.Rodrigues(rvec)
    print(rotationMatrix)
    print(tvec)

loadFile["rotation_matrix"] = rotationMatrix.tolist()
loadFile["translation_vector"] = tvec.tolist()

with open("cameraCalibration.json", "w") as fptr:
    json.dump(loadFile, fptr)