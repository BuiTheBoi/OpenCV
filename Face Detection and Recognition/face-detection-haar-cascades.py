# Haar cascades are easy to use, but are sensitive to noise...
# For example, some faces can be detected in places that are NOT faces.
# So to fix this, must adjust the MINIMUM NEIGHBORS

import cv2 as cv

img = cv.imread("../Images/rickroll_4k.jpg")

# NOTE: Face detection does NOT involve skintone or color
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier(
    "haar_face.xml")    # Reading in from xml file

# scaleFactor – Parameter specifying how much the image size is reduced at each image scale.
# minNeighbors – Parameter specifying how many neighbors each candidate rectangle should have to retain it.
#                Higher value results in fewer detections but with higher quality.

faces_rect = haar_cascade.detectMultiScale(  # This returns rectangular coordinates of the face as a list
    gray, scaleFactor=1.1, minNeighbors=10)

print(f"Number of faces found = {len(faces_rect)}")

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow("Detected Face", img)

cv.waitKey(0)
