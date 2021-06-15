#################################
# 1) Make an empty canvas
# 2) Draw Rectangle
# 3) Draw Circle
# 4) Draw Line
# 5) Print text on canvas
#################################

import cv2 as cv
import numpy as np


# Creating blank 2D array of all 0's but converted to image typ4
# Height and width of 500, and 3 color channels
blank = np.zeros((500, 500, 3), dtype="uint8")

cv.imshow("Blank", blank)  # Should show a black screen

# 1) Paint image a certain color
blank[:] = 0, 255, 0
cv.imshow("Green background", blank)

###################################################################################################

# 2) Paint rectangle
blank[:] = 0, 0, 0

# - from point (0, 0) to (250, 250) a green recrtangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
cv.imshow("Rectangle", blank)
###################################################################################################

# 3) Paint circle

# Drawing red circle in center with radius of 40 pixels
# NOTE: shape[0] means HEIGHT and shape[1] means WIDTH
cv.circle(blank, (blank.shape[1] // 2,
          blank.shape[0] // 2), 40, (0, 0, 255), thickness=3)
cv.imshow("Circle", blank)

###################################################################################################

# 4) Draw a line
# Draw a while line from (0, 0) to (250, 250)
cv.line(blank, (0, 0),
        (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=5)
cv.imshow("Line", blank)

###################################################################################################
# 5) Write text

# Write text starting from (255, 255) as FONT_HERSHEY_TRIPLEX font
# and a scale of 1.0
cv.putText(blank, "Hello", (225, 225), cv.FONT_HERSHEY_TRIPLEX,
           1.0, (255, 0, 0), thickness=2)
cv.imshow("Words", blank)

cv.waitKey(0)
