import cv2 as cv

# Image Display
def showImage(img, frames=-.10, window="Image"):
    key = ord('r')
    if frames < 0:
        while key != 27:
            cv.imshow(window, img)
            key = cv.waitKey(10)
    else:
        cv.imshow(window, img)
        key = cv.waitKey(frames)