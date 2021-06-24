# This program turns on webcam and counts down
# from 3 to 0.... Just testing out this feature for
# my later OpenCV/mediapipe project

import cv2 as cv
import mediapipe as md

capture = cv.VideoCapture(0)
numFrames = 0
countDown = 3
checkpoint_til_tick = 200

while True:
    flag, img = capture.read()

    cv.putText(img, str(countDown), (100, 100),
               cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 2)

    cv.imshow("You", img)
    print(f"Number of frames {numFrames}")
    numFrames += 1
    if(numFrames == checkpoint_til_tick and countDown != 0):
        countDown -= 1
        checkpoint_til_tick += 200

    if (cv.waitKey(30) & 0xff == 27):  # Press exit to close face cam
        break

capture.release()
cv.destroyAllWindows()
