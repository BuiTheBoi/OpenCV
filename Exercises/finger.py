# This program uses mediapipe and detects your hand
# which is then used to identify which finger is which


import cv2 as cv
import mediapipe as mp

times_tracked = 1

capture = cv.VideoCapture(0)
mpHand = mp.solutions.hands
hand = mpHand.Hands()

mpDraw = mp.solutions.drawing_utils

while True:
    flag, img = capture.read()

    img_RGB = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    tracked_img = hand.process(img_RGB)

    if (tracked_img.multi_hand_landmarks != None):
        print(f"Hand Tracked {times_tracked}")
        times_tracked += 1

        # Loop within scope of ALL HAND TRACKED
        for single_hand_landmarks in tracked_img.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, single_hand_landmarks,
                                  mpHand.HAND_CONNECTIONS)  # Draw landmarks

            # Loop within scope of all landmarks from EACH INDIV HAND
            for index, landmark in enumerate(single_hand_landmarks.landmark):
                # Get x and y coords of each landmark
                height, width, channel = img.shape
                x, y = int(width * landmark.x), int(height * landmark.y)

                # Identifying and printing finger types for a specific landmark
                if (index == 4):
                    cv.putText(img, "Thumb", (x, y + 5),
                               cv.FONT_HERSHEY_PLAIN, 1.1, (255, 0, 0), 2)
                elif (index == 8):
                    cv.putText(img, "Index", (x, y + 5),
                               cv.FONT_HERSHEY_PLAIN, 1.1, (255, 0, 0), 2)
                elif (index == 12):
                    cv.putText(img, "Middle", (x, y + 5),
                               cv.FONT_HERSHEY_PLAIN, 1.1, (255, 0, 0), 2)
                elif (index == 16):
                    cv.putText(img, "Ring", (x, y + 5),
                               cv.FONT_HERSHEY_PLAIN, 1.1, (255, 0, 0), 2)
                elif (index == 20):
                    cv.putText(img, "Pinky", (x, y + 5),
                               cv.FONT_HERSHEY_PLAIN, 1.1, (255, 0, 0), 2)
    cv.imshow("You", img)
    if (cv.waitKey(30) & 0xff == 27):
        break
