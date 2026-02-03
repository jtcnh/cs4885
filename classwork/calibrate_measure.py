"""
Calibration Measure
"""
import cv2 as cv
import numpy as np
import json
import math

# Assume:
# -> distortion is negligible
# -> skew is negligible

with open("cameraCalibration.json") as fptr:
    loadFile = json.load(fptr)

intrinsic_matrix = np.array(loadFile["intrinsic_matrix"])
rotation_matrix = np.array(loadFile["rotation_matrix"])
translation_vector = np.array(loadFile["translation_vector"])
dist_coeffs = np.array(loadFile["distortion_coeffs"])

# Focal length
# Obtain center px from intrinsic params.
fx = intrinsic_matrix[0][0]
fy = intrinsic_matrix[1][1]
cx = intrinsic_matrix[0][2]
cy = intrinsic_matrix[1][2]


# convert image uv to world point
def convert2d_to_3d(u : float, v : float):
    # translate image plane to camrea coordinates
    x = (u-cx)/fx
    y = (v-cy)/fy

    # get camera point & origin
    P_c = np.array([[x,y,1]]).T
    O_c = np.array([[0,0,0]]).T
    rotation_matrix_transpose = rotation_matrix.T

    # convert point & origin to world coordinate
    P_w = np.dot(rotation_matrix_transpose, (P_c - translation_vector))
    O_w = np.dot(rotation_matrix_transpose, (O_c - translation_vector))

    # construct the line through the real world plane
    line = P_w-O_w

    # solve for z oord of line
    line_z = line[2][0]
    world_origin_z = O_w[2][0]

    # find scalar k where: z = 0
    # 0 = owz + (k*lineZ)
    k = (-1)*(world_origin_z/line_z)
    P = O_w + k*(P_w - O_w)

    return P


def dist_between_points(p1, p2) -> np.float32:
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx*dx, dy*dy)


def midpoint(p1, p2) -> tuple[np.float32]:
    mx = round((p1[0]+p2[0])/2)
    my = round((p1[1]+p2[1])/2)
    return mx, my

# run a quick example
# point = convert2d_to_3d(93, 123)
# print(point)


two_point_array = []
def mouse_callback(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(f"{x} {y}")
        two_point_array.append([x,y])
        if len(two_point_array) > 1:
            key = ord("s")

cal_img = cv.imread("calibrationStarter.jpg")
key = ord("R")
cv.namedWindow("clickTwoPoints")
cv.setMouseCallback("clickTwoPoints", mouse_callback)

while key != 27:
    cv.imshow("clickTwoPoints", cal_img)
    key = cv.waitKey(10)
    if len(two_point_array) > 1:
        break
    cv.destroyAllWindows()

print("Points Clicked")
print(two_point_array)

# Convert the points
wp1 = convert2d_to_3d(two_point_array[0][0], two_point_array[0][1])
wp2 = convert2d_to_3d(two_point_array[1][0], two_point_array[1][1])

print("Points:")
print(wp1)
print(wp2)

dist = dist_between_points(wp1, wp2)
print("Distance Between Points")
dist = round(dist, 2)
print(dist)

# visualization
key = ord("r")
new_img = cv.line(cal_img, wp1, wp2, (255,0,0), 5)
mx, my = midpoint(wp1, wp2)
print(f"Midpoint: {mx} {my}")

# new image
new_img = cv.putText(new_img,str(dist),(mx, my-10),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv.LINE_AA)

# display image
# cv.imshow(...)