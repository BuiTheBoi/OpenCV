########################
# Simple thresholding
# Inverse thresholding
# Adaptive thresholding
########################

from typing import ClassVar
import cv2 as cv

img = cv.imread("Images/Leaves.jpeg")


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

####################################################################################

# Simple Thresholding

# Threshold value is 150
# if greater than 150, then set pixel to 255
# with thresholding type as binary type.
# (Threshold holds the 150 value, whole thresh has the thresholded image)
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple thresholded", thresh)

####################################################################################

# Inverse thresholding

# Now if greater than thresholded value (150) then it is
# black, and vice versa
threshold, thresh_inverse = cv.threshold(
    gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Thresholded Inverse", thresh_inverse)

####################################################################################

# Adaptive thresholding

# Letting computer find optimal thresholding value
# and binarizes image

# cv.ADAPTIVE_THRESH_MEAN_C means setting threshold value as mean of neighboring pixels
# Second to last parameter (11) is block (kernel) size used to compute optimal threshold value
# The last parameter (3) is the "C value" which is subtracted from the mean (The more subtracted the more accurate)
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive Thresholding", adaptive_thresh)

cv.waitKey(0)
