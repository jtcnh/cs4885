import cv2 as cv
import json

"""
Export Image
"""
webcam = cv.VideoCapture(0)
key = ord("k")

# while (key != 27):
#     img = webcam.read()
#     key = cv.waitKey()




"""
Click to Calibrate
"""
actualPoints = [
    [40, 40, 0],
    [160, 40, 0],
    [40, 160, 0],
    [160, 160, 0]
]

imgSensorPoints = []

def mouseCallback(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        print(f"{x} {y}")
        imgSensorPoints.append([x,y])

calibrateImage = cv.imread("calibrateImage.jpg")
cv.namedWindow("calibrate")
cv.setMouseCallback("calibrate", mouseCallback)

while key != 27:
    cv.imshow("calibrate", calibrateImage)
    key = cv.waitKey()

print(imgSensorPoints)


# Load camera calibration
with open("cameraCalibration.json", "r") as f:
    loadFile = json.load(f)

loadFile["imgPts"] = imgSensorPoints

with open("cameraCalibration.json", "w") as f:
    json.dump(loadFile, f)