import io
import json


"""
Export Calibration
"""
calJsonFile = io.open("cameraCalibration.json", "w")
export = json.dump({
    "Test":1,
    "Another":2
}, calJsonFile)
calJsonFile.close()


"""
Import Calibration
"""
calImport = io.open("cameraCalibration.json", "r")
x = json.load(calImport)
print(x)
calImport.close()