"""
Code Along 0
Jack Chambers

OpenCV Basics


"""
import cv2 as cv

imagePath = "../images/octopus.jpg"
KEY_ESCAPE = 27

# import an image
# img = cv.imread("../images/chungus.png")

# print(type(img))
# print(img.shape)

"""
Open an image in a window
"""

def openImage(img):
    key = ord("r")
    while key != KEY_ESCAPE:
        cv.imshow("Opened Image", img)
        key = cv.waitKey()
    cv.destroyAllWindows()


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
# img = cv.imread(imagePath)
# img = img[250:500, 400:700]

# # define border
# borderSize = 10
# borderColor = [255, 0, 0]

# img = cv.copyMakeBorder(img, borderSize, borderSize, borderSize, borderSize, cv.BORDER_CONSTANT, value=borderColor)


"""
    Writing out an image
"""
# img = cv.imread(imagePath)
# path = "octopus_copy.png"

# cv.imwrite(path, img)


"""
    Write Text on Image
"""
img = cv.imread(imagePath)

# write text
def text(img, text, 
        org=(100,225), 
        font=cv.FONT_HERSHEY_SIMPLEX, 
        fontScale=1, 
        color=(255,255,255), 
        thickness=2,
        lineType = cv.LINE_AA
    ):
    
    newImg = img.copy() # images are pass by reference, not copies
    cv.putText(newImg, text, org, font, fontScale, color, thickness, lineType)
    return newImg

# draw rectangle
newImg = text(img, "octopus: 98%")
newImg = cv.rectangle(newImg, (100,250), (900,600), (0,255,0), 3)

openImage(newImg)