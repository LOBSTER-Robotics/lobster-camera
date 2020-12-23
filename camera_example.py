#!/bin/python3

import cv2

# print openCV version
from Camera import Camera, CameraMode, VideoFormats

print("Using openCV version ", cv2.__version__)

#  camera = Camera.fromEnum(CameraMode.RAW_480_30)
camera = Camera(960,540,15,VideoFormats.mjpeg)

while(True):
    ret = camera.captureFrame()
    if ret is True:
        # Waits for a user input to quit the application
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # the camera failed to record a frame so abort
        break

camera.release()
