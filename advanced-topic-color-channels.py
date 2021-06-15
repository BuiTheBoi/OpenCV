import cv2 as cv
import numpy as np  # Used to make a blank image

img = cv.imread("images/Leaves.jpeg")
cv.imshow("Leaf", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# This shows the intensity of each color
# Which is why it is in grayscale, but each can be lighter or darker
b, g, r = cv.split(img)

cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

# Merging images to not make them color scale
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merging b, g, r images together to original
merged = cv.merge([b, g, r])
cv.imshow("Merged Image", merged)

cv.waitKey(0)
