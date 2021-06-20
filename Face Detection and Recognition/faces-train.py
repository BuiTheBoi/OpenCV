# This program takes in photos of different people
# and does a process of Deep Learning to recognize
# who these people are.

import os
import cv2 as cv
import numpy as np


if __name__ == "__main__":
    people = []
    for i in os.listdir(r"C:\Users\Justin\Documents\Python\OpenCV\Face Detection and Recognition\Faces"):
        # Appends the list of names of people in Faces folder
        people.append(i)

    # Base folder referencing Faces directory
    DIR = r"C:\Users\Justin\Documents\Python\OpenCV\Face Detection and Recognition\Faces"

    haar_cascade = cv.CascadeClassifier("haar_face.xml")

    # Training set
    features = []   # Characterisitcs/features of faces
    labels = []     # Who's face it belongs to

    # -------------------------------------------------------------------------------------

    # This function appends the features and labels array as it reads through each person
    # and each face
    def create_train():
        for person in people:
            # Gets the path of the person in faces
            path = os.path.join(DIR, person)
            label = people.index(person)    # index() returns position in array

            # Taking images of EACH person's folder
            for img in os.listdir(path):
                # Gets path of individual image
                img_path = os.path.join(path, img)
                img_array = cv.imread(img_path)  # Stores an image

                gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

                faces_rect = haar_cascade.detectMultiScale(
                    gray, scaleFactor=1.1, minNeighbors=4)

                for (x, y, w, h) in faces_rect:  # Loop through every face within photo
                    face_region_of_interest = gray[y:y + h, x:x + w]
                    features.append(face_region_of_interest)
                    labels.append(label)    # Index of people[]

    # -------------------------------------------------------------------------------------

    create_train()
    print("Training successful>>>>>>>>>>>>>>>>>>>>>>>>")

    # ----------------- Training our recognizer -----------------

    # Convert features[] and labels[] to numpy arrays
    features = np.array(features, dtype="object")
    labels = np.array(labels)

    face_recognizer = cv.face.LBPHFaceRecognizer_create()   # Instantiate face recognizer

    # Train recognizer on the features list and the labels list
    face_recognizer.train(features, labels)

    # Saving into YAML (yml) file so that we can use this in
    # another file/directory... in other words make it more dynamic
    face_recognizer.save("face_trained.yml")

    np.save("features.npy", features)
    np.save("labels.npy", labels)
