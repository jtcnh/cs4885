"""
Code Along 1
1/27/2026

Calibration from Chessboard
Updated 2/11/2026 to write to file

"""
import cv2 as cv
import numpy as np
import json

def LoadCalibration(fileName):
    with open(fileName, "r") as fptr:
        load_file = json.load(fptr)

    dist_coefs = np.zeros((4,1))
    #obj_pts = np.array(actual_points).astype(np.float32)
    #img_pts = np.array(load_file["img_points"]).astype(np.float32)
    i_mtx = np.array(load_file['intrinsic_matrix'])
    dist_coefs = np.array(load_file['distortion_coefficients'])

    return {
        'intrinsic_matrix' : i_mtx,
        'distortion_coefficients' : dist_coefs
    }


def SaveCalibration(fileName, calibrationDictionary):
    # need to convert to list for json serialize
    dc = calibrationDictionary['distortion_coefficients']
    calibrationDictionary['distortion_coefficients'] = dc.tolist()
    imtx = calibrationDictionary['intrinsic_matrix']
    calibrationDictionary['intrinsic_matrix'] = imtx.tolist()

    # export with file ptrs
    with open(fileName, "w") as calibrationFilePtr:
        json.dump(calibrationDictionary, calibrationFilePtr)


#https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html
def Undistort(originalImg, calibrationDict):
    i_mtx = calibrationDict['intrinsic_matrix']
    dcoefs = calibrationDict['distortion_coefficients']

    h,w = originalImg.shape[:2]
    newCameraMtx, roi = cv.getOptimalNewCameraMatrix(i_mtx, dcoefs, (w,h), 1, (w,h))

    # undistort
    newImg = cv.undistort(originalImg, i_mtx, dcoefs, None, newCameraMtx)
    
    # crop new image
    x,y,w,h = roi
    newImg = newImg[y:y+h, x:x+w]
    
    # output new image
    return newImg


# create a calibration function
def CreateCalibration():
    # Variables
    nValidImages = 0
    rowCorners = 9
    columnCorners = 6
    objPtsArray = []
    imgPtsArray = []
    patternSize = (rowCorners, columnCorners)
    key = ord("k")
    webcam = cv.VideoCapture(0)

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
            imgPath = f"./exportedImages/image{nValidImages}.jpg"
            cv.imwrite(imgPath, raw)

            # show image
            cv.imshow("Image", raw)
            key = cv.waitKey(50)
        else:
            cv.imshow("Image", raw)
            key = cv.waitKey(10)


    # Save calibration to file
    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(
        objPtsArray, 
        imgPtsArray, 
        gray.shape[::-1], 
        None, 
        None
    )

    # convert vector tuple to array
    rotationVectorArray = [rv.tolist() for rv in rvecs]
    translationVectorArray = [tv.tolist() for tv in tvecs]
    
    return {
        "float" : ret,
        "intrinsic_matrix" : mtx,
        "distortion_coefficients" : dist,
        "rotation" : rotationVectorArray,
        "translate" : translationVectorArray
    }