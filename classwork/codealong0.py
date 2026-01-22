"""
Code Along 0
Jack Chambers

OpenCV Basics


"""
import cv2 as cv

imagePath = "../images/octopus.jpg"

# import an image
# img = cv.imread("../images/chungus.png")

# print(type(img))
# print(img.shape)

"""
Open an image in a window
"""
# key = ord("r")
# while key != ord("s"):
#     cv.imshow("Picture", img)
#     key = cv.waitKey()
# cv.destroyAllWindows()


"""
    Accessing the webcam
"""
# webcam = cv.VideoCapture(0)
# key = ord("r")
# while key != 27:
#     still = webcam.read()
#     print(still)
#     cv.imshow("Webcam Feed", still[1])
#     key = cv.waitKey(10) # in ms
#     print(key)
# cv.destroyAllWindows()



"""
    Accessig image pixels
"""
# img = cv.imread(imagePath)
# # row, column, channel
# # BGR color space

# ## Blue Intensity
# # pixel 40, 40
# print(img[40,40,0])
# print(img.dtype)


"""
    Image Indexing and Borders
"""