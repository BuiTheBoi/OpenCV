import cv2 as cv

img = cv.imread("Images/leaves.jpeg")

###########################################################################

# Averaging - Taking the average of pixels surrounding the center pixel
avg = cv.blur(img, (3, 3))  # The higher kernel size, the more blur
cv.imshow("Average Blur", avg)

###########################################################################

# Gausian - Each surrounding pixel is given a weight. The
#           products of the weight give the value for center
gauss = cv.GaussianBlur(img, (3, 3), 0)  # 0 represents standard deviation
cv.imshow("Gaussian Blur", gauss)

###########################################################################

# Median - Same as average, but now finds median
# Kernel size automatically assumed to be a single integer (n x n)
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

###########################################################################

# Bilateral - (Most effective) Blurrs but retains edges in image
# Diameter is 5
# A larger sigma color means there are more colors in neighborhood considered
# Larger values of space sigma means pixels further out from central pixel
bilateral = cv.bilateralFilter(img, 10, sigmaColor=35, sigmaSpace=25)
cv.imshow("Bilateral Blur", bilateral)


cv.waitKey(0)
