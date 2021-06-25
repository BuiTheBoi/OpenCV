import cv2 as cv
import mediapipe as mp
import os
import time
import HandTrackingModule as htm

cap = cv.VideoCapture(0)

# Setting width and height of camera
wCam, hCam = 640, 480
cap.set(3, wCam)
cap.set(4, hCam)

# Storing Fingers images into list
folderPath = "Fingers"
myList = os.listdir(folderPath)  # Paths (Strings) for each finger image
overlayList = []                # Contains the actual images after reading

for imPath in myList:
    image = cv.imread(f"{folderPath}/{imPath}")
    overlayList.append(image)

pTime = 0
detector = htm.hand_detector(detection_confidence=0.75)

tipIDs = [4, 8, 12, 16, 20]

while True:
    flag, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        if (lmList[tipIDs[0]][1] > lmList[tipIDs[0]-1][1]):   # x axis of thumb tip
            fingers.append(1)   # Finger opened
        else:
            fingers.append(0)   # Finger closed

        # Pointer, middle, ring, pinky fingers
        for id in range(1, 5):
            # If landmark at whichever finger tip is at higher position than
            # landmark below it
            if (lmList[tipIDs[id]][2] < lmList[tipIDs[id]-2][2]):
                fingers.append(1)   # Finger opened
            else:
                fingers.append(0)   # Finger closed

        totalFingers = fingers.count(1)
        print(f"{totalFingers} Fingers Tracked")

        h, w, channel = overlayList[totalFingers-1].shape
        # Limit of my heights and widths are 0:200, respectively
        img[0:h, 0:w] = overlayList[totalFingers-1]

    # Getting FPS
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv.putText(img, f"FPS: {int(fps)}", (400, 70),
               cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv.imshow("You", img)

    if (cv.waitKey(30) & 0xff == 27):
        break
