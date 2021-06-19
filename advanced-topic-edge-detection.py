import cv2 as cv
import numpy as np

img = cv.imread("Images/Leaves.jpeg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#######################################################################################

# Laplacian Edge Detection

# This method computes the gradients of the grayscale image
lap = cv.Laplacian(gray, cv.CV_64F)

# This is so that pixels cannot have negative values,
# which then gets converted to an image datatype
lap = np.uint8(np.absolute(lap))


cv.imshow("Laplacian", lap)

#######################################################################################

# Sobel Edge Detection

# This computes gradients in x and y directions
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)    # x direction = 1, y direction = 0
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)    # x direction = 0, y direction = 1

cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)


# Combining both x and y sobels
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow("Combined Sobel", combined_sobel)

#######################################################################################

# Canny Edge Detection (Advanced method as it uses multiple steps including sobel)

# Two threshold values of 150 and 175
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)


cv.waitKey(0)
