"""
Elliot Greenlee
Date Started: 2018-01-19
University of Tennessee, Knoxville: WIND
"""

# Imports
import cv2
import time
import logging
import argparse

# Constants
mac_webcam_fps = 15
mac_webcam_frame_delay = 2
default_camera = 0
default_file = "data/output.mp4"

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str,
                    help="file to which the video is written")
parser.add_argument('--verbosity', type=int,
                    choices=[logging.NOTSET, logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
                             logging.CRITICAL],
                    default=logging.INFO,
                    help="increase output verbosity")
parser.add_argument('--fps', type=float, default=mac_webcam_fps,
                    help="write fps should match camera record fps")
parser.add_argument('--camera', type=int, choices=[0, 1], default=default_camera,
                    help="select the input camera")
args = parser.parse_args()

# Logging
logging.basicConfig(level=args.verbosity)

# Start obtaining video data
logging.info("Starting up")
video_capture = cv2.VideoCapture(args.camera)

# Define the codec and create VideoWriter object
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(args.filename, fourcc, args.fps, (width, height))

# Record data until halted
logging.info("Beginning recording at {}".format(time.time()))
capturing = video_capture.isOpened()
while capturing:
    # Capture the current frame
    capturing, frame = video_capture.read()
    logging.debug("Current frame time: {}".format(time.time()))

    # Write the current frame
    out.write(frame)

    # Show the frame being recorded
    cv2.imshow('frame', frame)

    # Press q to stop
    if cv2.waitKey(1) == ord('q'):
        logging.debug("The operator pressed q so recording will stop")
        logging.info("Stopping recording at {}".format(time.time()))
        break

# Release everything if job is finished
logging.info("Shutting down")
video_capture.release()
out.release()
cv2.destroyAllWindows()
