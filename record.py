"""
Elliot Greenlee
Date Started: 2018-01-18
University of Tennessee, Knoxville: WIND
"""

import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('data/time.mp4', fourcc, 15, (width, height))

i = 0
while cap.isOpened():
    ret, frame = cap.read()
    print(int(cap.get(cv2.CAP_PROP_FPS)))
    if i % 20 == 0:
        print(i, time.time())
    i += 1

    if ret:
        # write the frame
        out.write(frame)

        # Show the frame being recorded
        cv2.imshow('frame', frame)

        # Quit recording if q is pressed
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()