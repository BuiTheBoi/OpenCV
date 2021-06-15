# This program takes an image of a babushka doll
# and using cv.imshow, print many instances of the doll
# but each instance is a smaller instance of the previous.
# This requires us to implement a reshape() image function

import cv2 as cv


def reshape(frame, percentage=0.60):
    height = int(frame.shape[0] * percentage)
    width = int(frame.shape[1] * percentage)

    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)


if __name__ == "__main__":
    large_img = cv.imread(
        "Images/49648819-russian-nesting-dolls-babushkas-or-matryoshkas-one.jpg")

    cv.imshow("Large Doll", large_img)

    med_img = reshape(large_img)
    cv.imshow("Medium Doll", med_img)

    small_img = reshape(med_img)
    cv.imshow("Small Doll", small_img)

    cv.waitKey(0)
