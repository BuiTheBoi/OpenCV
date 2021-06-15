import cv2 as cv


# Rescalling an image (Also works for vids)
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Another method to rescale videos (Not images though)
# More specifically, LIVE VIDEOS (i.e face cams)
def changeRes(width, height):
    capture.set(3, width)   # 3 references width
    capture.set(4, height)  # 4 references height


if __name__ == "__main__":

    capture = cv.VideoCapture("Videos/Aquarium-Adventures.mov")

    while True:
        isTrue, frame = capture.read()

        # Resizing each frame of the video
        frame_resized = rescaleFrame(frame, 0.1)

        cv.imshow("Video", frame)
        cv.imshow("Video Resized", frame_resized)

        # Condition for if letter 'd' is pressed then break out of loop
        if cv.waitKey(20) & 0xFF == ord("d"):
            break

    capture.release()   # Closes video file or capturing device.. deallocates this pointer
    cv.destroyAllWindows()  # Destroy all the windows created
