import cv2
import numpy
import random

if __name__ == "__main__":
    black = (0, 0, 0)

    # Making the Canvas to draw on
    # Canvas of height 800 and width 1200
    canvas = numpy.zeros((800, 1200, 3), dtype="uint8")
    canvas[:] = 255, 255, 255

    # Printing a bunch of circles
    for _ in range(100):
        cv2.circle(canvas, (random.randint(0, 1200), random.randint(0, 800)), random.randint(
            25, 50), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), random.randint(0, 15))

    cv2.line(canvas, (0, 450), (1200, 450), (random.randint(0, 200), random.randint(
        0, 200), random.randint(0, 200)), random.randint(5, 45))

    cv2.line(canvas, (1010, 0), (1010, 800), (random.randint(0, 200), random.randint(
        0, 200), random.randint(0, 200)), random.randint(5, 45))

    # Creating the title
    cv2.rectangle(canvas, (585, 350), (945, 450), black, cv2.FILLED)
    cv2.putText(canvas, "Welcome to My Art!", (canvas.shape[1] // 2, canvas.shape[0] // 2),
                cv2.FONT_HERSHEY_TRIPLEX, 1.0, (100, 100, 255), thickness=4)

    cv2.imshow("Canvas", canvas)

    cv2.waitKey(0)

    # Image size: 1200 x 800
    # img = cv2.imread("Images/Nighthawk_Front.jpg")
    # cv2.imshow("Figher Jet", img)

    cv2.waitKey(0)
