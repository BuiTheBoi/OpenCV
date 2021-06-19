###################################
# Grayscale and Colored histogram #
###################################

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Images/Leaves.jpeg")

blank = np.zeros(img.shape[:2], dtype="uint8")


#####################################################################################

# GRAYSCALE HISTOGRAM

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

masked = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow("Masked Gray Image", masked)


# This method computes histogram for a list of images
# Also takes in the number of channels
gray_hist = cv.calcHist([gray], channels=[0], mask=mask,
                        histSize=[256], ranges=[0, 256])

# Plotting on matplotlib
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")  # Represents intensity levels
plt.ylabel("# of pixels")   # Number pixels are dependent on intensity levels
plt.plot(gray_hist)
plt.xlim([0, 256])  # Giving limit across x axis
plt.show()

cv.waitKey(0)

#####################################################################################

# COLORED HISTOGRAM

mask2 = cv.circle(
    blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

masked2 = cv.bitwise_and(img, img, mask=mask2)
cv.imshow("Masked Image", masked2)

colors = ('b', 'g', 'r')    # Tuple of color channels

plt.figure()
plt.title("Colored Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

for i, col in enumerate(colors):
    hist2 = cv.calcHist([img], channels=[i], mask=mask2,
                        histSize=[256], ranges=[0, 256])
    plt.plot(hist2, color=col)
    plt.xlim([0, 256])

plt.show()  # This shows pixel intensity of all 3 channels

cv.waitKey(0)

# --------------------------------------------------------------
# NOTE: The channels parameter in cv.calcHist()
#       has blue = [0], green = [1], red = [2].
#       But grayscale images are automatically considered
#       as channel = [0]
# --------------------------------------------------------------
