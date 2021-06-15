import cv2 as cv

# -------------------------- Reading images --------------------------
img = cv.imread("Images/Mona-Lisa.jpg")

# Printing this image with the name and actual read image
cv.imshow("Mona Lisa", img)

cv.waitKey(0)   # Waits for specific delay (milliseconds) for key to be pressed


# -------------------------- Reading videos --------------------------
capture = cv.VideoCapture("Videos/Aquarium-Adventures.mov")

# Reading video frame by frame and returning boolean if it succesfully read
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    # Condition for if letter 'd' is pressed then break out of loop
    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()   # Closes video file or capturing device.. deallocates this pointer
cv.destroyAllWindows()  # Destroy all the windows created
