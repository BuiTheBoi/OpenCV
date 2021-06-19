# Using the knowledge of what we've learned so far with masking images,
# this program masks circles together to make a cool olympics logo

from typing import final
import cv2 as cv
import numpy as np

flags = cv.imread("Images/the-world-flag.jpg")  # Image of flags in the world

canvas = np.zeros((flags.shape[:2]), dtype="uint8")    # Empty black image

# Coordinate reference to circle1 (See below)
x_coordinate_origin = 125
y_coordinate_origin = 110

##################################### Drawing circles #####################################

# Drawing circles on row 1
circle1 = cv.circle(
    canvas.copy(), (x_coordinate_origin, y_coordinate_origin), 100, 255, thickness=7)

circle2 = cv.circle(
    canvas.copy(), (x_coordinate_origin + 130, y_coordinate_origin), 100, 255, thickness=7)

circle3 = cv.circle(
    canvas.copy(), (x_coordinate_origin + 260, y_coordinate_origin), 100, 255, thickness=7)

# Drawing circles on row 2
circle4 = cv.circle(
    canvas.copy(), (x_coordinate_origin + 65, y_coordinate_origin + 130), 100, 255, thickness=7)

circle5 = cv.circle(
    canvas.copy(), (x_coordinate_origin + 195, y_coordinate_origin + 130), 100, 255, thickness=7)

###############################################################################################

# Masking all of the circles together
mask = cv.bitwise_or(circle1, circle2)
mask = cv.bitwise_or(mask, circle3)
mask = cv.bitwise_or(mask, circle4)
mask = cv.bitwise_or(mask, circle5)

final_img = cv.bitwise_and(flags, flags, mask=mask)
final_img = cv.putText(final_img, "INTERNATIONAL OLYMPICS",
                       (40, 380), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), thickness=2)


cv.imshow("Masked Image", final_img)


cv.waitKey(0)
