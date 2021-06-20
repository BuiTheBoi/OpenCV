import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier("haar_face.xml")

people = []
for i in os.listdir(r"C:\Users\Justin\Documents\Python\OpenCV\Face Detection and Recognition\Faces"):
    # Appends the list of names of people in Faces folder
    people.append(i)

# features = np.load("features.npy")
# labels = np.load("labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()   # Instantiate face recognizer
face_recognizer.read("face_trained.yml")

img = cv.imread(
    r"C:\Users\Justin\Documents\Python\OpenCV\Face Detection and Recognition\Faces\Jeff Cavalier\jeff.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Unidentified Person", gray)

# Detect the face in the image
# NOTE: scale factor = 1.1 and neighbors = 4
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    face_region_of_interest = gray[y:y + h, x:x + w]

    label, confidence_value = face_recognizer.predict(face_region_of_interest)
    print(f"Label = {people[label]} with a confidence of {confidence_value}")

    cv.putText(img, str(people[label]), (20, 20),
               cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow("Detected Face", img)

cv.waitKey(0)
