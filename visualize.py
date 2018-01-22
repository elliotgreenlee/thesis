"""
Elliot Greenlee
Date Started: 2018-01-22
University of Tennessee, Knoxville: WIND
"""
import numpy as np
import cv2
from target import Target

green = (0, 255, 0)
left_boundary = -45
right_boundary = 45


def visualize(frame, targets, angle):

    # Add rectangles around each target
    for target in targets:
        cv2.rectangle(frame, target.rectangle[0], target.rectangle[1], green)
        # TODO: Add a small text box with the object type on each target
        # TODO: target.object_type

    direction = angle
    if direction < left_boundary:
        triangle = np.array([[0, 0], [0, 100], [50, 50]], np.int32)
        cv2.polylines(frame, [triangle], True, green)
    if direction > right_boundary:
        triangle = np.array([[0, 0], [0, 100], [50, 50]], np.int32)
        cv2.polylines(frame, [triangle], True, green)


    cv2.imshow('frame', frame)

    return frame
