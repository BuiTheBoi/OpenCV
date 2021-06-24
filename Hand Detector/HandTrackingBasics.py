import cv2 as cv
import mediapipe as mp  # Hand and finger tracking solution library
import time


cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()  # Making an instance

# To draw all the points when hand is tracked
mpDraw = mp.solutions.drawing_utils

pTime = 0   # Previous time
cTime = 0   # Current time

while True:
    flag, img = cap.read()
    # Must be converted to RGB before usage
    img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(img_RGB)

    if(results.multi_hand_landmarks != None):  # If a hand is tracked
        for hand_landmarks in results.multi_hand_landmarks:
            # landmark returns ratio of images
            for index, landmark in enumerate(hand_landmarks.landmark):
                height, width, channel = img.shape  # Gets width and height
                center_x, center_y = int(   # To get x and y coordinates
                    landmark.x * width), int(landmark.y * height)
                print(index, center_x, center_y)

                if (index == 0):    # Draws large pink circle at landmark 0 (Wrist)
                    cv.circle(img, (center_x, center_y),
                              15, (255, 0, 255), cv.FILLED)

            # hand_landmarks represent the red points
            # mpHands.HAND_CONNECTIONS draws the green lines
            mpDraw.draw_landmarks(img, hand_landmarks,
                                  mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (10, 70),
               cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)

    cv.imshow("You", img)
    # Press 'd' to exit
    if cv.waitKey(20) & 0xFF == ord("d"):
        break
