##################################
# 1) Grayscale
# 2) Blur
# 3) edge cascade
# 4) Dilate edges
# 5) Erode edges
# 6) resized
# 7) Crop
##################################


import cv2 as cv

#####################################################################################

# Original BGR
img = cv.imread("Images/ALR2.jpg")
cv.imshow("Original", img)

#####################################################################################

# 1) Converting BGR images to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#####################################################################################

# 2) Blurring an image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)  # (7 x 7) kernel size
cv.imshow("Blur", blur)

#####################################################################################

# 3) Edge cascade
canny = cv.Canny(img, 125, 175)  # Threshold values of 125 and 175
cv.imshow("Canny Edges", canny)

#####################################################################################

# 4) Dilating the image
# Essentially makes the edges thicker
# Kernel size of (8 x 8) with 6 iterations
dilated = cv.dilate(canny, (8, 8), 6)

cv.imshow("Dilated", dilated)

#####################################################################################

# 5) Eroding a dilated image
# Makes the edges thinner
eroded = cv.erode(dilated, (8, 8), 6)
cv.imshow("Eroded", eroded)

#####################################################################################

# 6) Resize
# Resizing an image to 500 x 500 ignoring the aspect ratio
resized = cv.resize(img, (500, 500))
cv.imshow("Resized", resized)

#####################################################################################

# 7) Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
