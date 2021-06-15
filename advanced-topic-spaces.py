import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Images/Mona-Lisa.jpg")
cv.imshow("Original", img)


# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

# BGR to HSV (Heu Saturation Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("L*A*B", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_RGB2BGR)
cv.imshow("RGB", rgb)

cv.waitKey(0)

###########################################################################

# ------------------ Difference between BGR and RGB? ------------------
# Matplotlib interprets images as RGB, therefore it leads to inverted
# colors compared to OpenCV

# Uncomment and run these lines:
# plt.imshow(img)
# plt.show()
