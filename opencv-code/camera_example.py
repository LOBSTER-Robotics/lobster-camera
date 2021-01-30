#!/usr/bin/env python3

import cv2

# print openCV version
from Camera import Camera, CameraMode, VideoFormats

print("Using openCV version ", cv2.__version__)

#  camera = Camera.fromEnum(CameraMode.RAW_480_30)
camera = Camera(960,540,15,VideoFormats.mjpeg)

frame_count = 0
max_time = 5
max_frames = 15 * max_time

while(True):
    ret = camera.captureFrame()
    if ret is True and frame_count < max_frames:
        # Waits for a user input to quit the application
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # the camera failed to record a frame so abort
        # or the max number of frames is exceeded
        if frame_count >= max_frames:
            print("Maximum recording time exceeded")
        break

    frame_count +=1

camera.release()
