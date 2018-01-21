"""
Elliot Greenlee
Date Started: 2018-01-18
University of Tennessee, Knoxville: WIND
"""

import numpy as np
import cv2


def main():
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture("filename")

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.flip(gray, 1)

        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return

if __name__ == "__main__":
    main()
