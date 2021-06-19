#########################
# Translating
# Rotating
# Resizing
# Flipping
# Cropping
#########################

import cv2 as cv
import numpy as np


def translate(img, x, y):   # Translation
    transMat = np.float32([[1, 0, x], [0, 1, y]])   # Translation matrix
    dimensions = (img.shape[1], img.shape[0])       # Dimensions
    return cv.warpAffine(img, transMat, dimensions)

    # If you have negative values for x, you are shifting image to the left
    # but positive values are shifted right.

    # If you have negative values for y, you are shifting image up
    # but positive values are shifted down.


def rotate(img, angle, rotPoint=None):   # Rotate
    (height, width) = img.shape[:2]

    if rotPoint is None:    # Assume to rotate around the center if rotation point is none
        rotPoint = (width // 2, height // 2)
    # NOTE: the 1.0 represents the scale
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


if __name__ == "__main__":
    img = cv.imread("Images/Leaves.jpeg")

    ######################################################################

    # Translating images
    translated = translate(img, -100, 100)
    cv.imshow("Translate", translated)

    ######################################################################

    # Rotating images
    # Positive angles represent rotating counterclockwise... vice versa
    rotated = rotate(img, 45)
    cv.imshow("Rotated", rotated)

    rotated_rotated = rotate(rotated, 45)
    cv.imshow("Rotated rotated", rotated_rotated)
    ######################################################################

    # Resizing
    # INTER_AREA is default
    resized = cv.resize(img, (330, 330), interpolation=cv.INTER_CUBIC)
    cv.imshow("Resized", resized)

    ######################################################################

    # Flipping
    # Flip codes (Second parameter):
    #   0: Flip image vertically over x axis
    #   1: Flip image horizintally over y axis
    #  -1: Combination of 0 and 1

    flip = cv.flip(img, 1)
    cv.imshow("Flip", flip)

    ######################################################################

    # Cropping
    cropped = img[120:130, 200:220]
    cv.imshow("Cropped", cropped)

    cv.waitKey(0)
