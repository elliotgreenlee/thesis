"""
Elliot Greenlee
Date Started: 2018-01-18
University of Tennessee, Knoxville: WIND
"""

import numpy as np
import cv2
from target_detector import detect_targets
from target import Target
from tracker import Tracker
from directionality import aggregator, direction
from visualize import visualize


def main():  # TODO: pass variable to main that switches between recording and reading

    # Start obtaining nuclear data
    # TODO: Setup pipe?
    # TODO: open file

    # Start obtaining video data
    video_capture = cv2.VideoCapture(0)
    #video_capture = cv2.VideoCapture("filename")

    # Capture the first frame
    capturing, frame = video_capture.read()

    # Detect objects in the frame
    targets = detect_targets(frame)

    # Initialize the tracker
    tracker = Tracker(frame, targets)

    while capturing:
        # Extract counts from file for the last frame
        counts = aggregator()

        # Find angle from directionality
        angle = direction(counts)

        # Capture the current frame
        capturing, frame = video_capture.read()

        # Update the target locations for the current frame
        targets = tracker.track(frame, targets)

        # Visualize the resulting frame
        visualize(frame, targets, angle)

        # Press q to stop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Close out application
    video_capture.release()
    cv2.destroyAllWindows()
    return

if __name__ == "__main__":
    main()
