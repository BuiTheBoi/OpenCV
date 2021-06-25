# Creating a hand tracking module to use for future projects

import cv2 as cv
import mediapipe as mp
import time


class hand_detector():
    # Constructor
    def __init__(self, mode=False, max_hands=2, detection_confidence=0.5, track_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.track_confidence = track_confidence

        # Initializations
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.max_hands, self.detection_confidence, self.track_confidence)
        self.mpDraw = mp.solutions.drawing_utils

    # Sees if there is a hand that exists on camera
    def findHands(self, img, draw=True):
        # Must be converted to RGB before usage
        img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(img_RGB)  # Gets all of the landmarks

        if(self.results.multi_hand_landmarks != None):  # If a hand is tracked
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, hand_landmarks,
                                               self.mpHands.HAND_CONNECTIONS)
        return img  # Returns image with drawing

    # Finds the coordinates for chosen landmark on hand
    def findPosition(self, img, handNo=0, draw=True):
        landmark_list = []
        if(self.results.multi_hand_landmarks != None):
            # In case if there were multiple hands
            myHand = self.results.multi_hand_landmarks[handNo]

            for index, landmark in enumerate(myHand.landmark):
                height, width, channel = img.shape  # Gets width and height
                center_x, center_y = int(   # To get x and y coordinates
                    landmark.x * width), int(landmark.y * height)
                landmark_list.append([index, center_x,  center_y])

                if (draw):  # Draw large pink circle on desired landmark if True
                    cv.circle(img, (center_x, center_y),
                              25, (255, 0, 255), cv.FILLED)

        return landmark_list


def main():
    cap = cv.VideoCapture(0)

    pTime = 0   # Previous time
    cTime = 0   # Current time
    detector = hand_detector()  # Instance of class made

    while True:
        flag, img = cap.read()
        img = detector.findHands(img)
        lm_list = detector.findPosition(img)

        if (len(lm_list) != 0):
            print(lm_list[4])   # Shows only landmark 4

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv.putText(img, str(int(fps)), (10, 70),
                   cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)

        cv.imshow("You", img)
        # Press 'd' to exit
        if cv.waitKey(20) & 0xFF == ord("d"):
            break


if __name__ == "__main__":
    main()
