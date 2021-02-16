# Lobster-camera
This is the camera recording software for the lobster robot. It uses v4l2-ctl to
record the camera. It will be optimized for running on a raspberry pi 4 with a
usb 3.0 v4l2 camera.

# Installation

## required packages (Ubuntu):
- python3
- v4l2-utils

You will also need a POSIX shell

You can now test if it works by running `v4l2-command.sh -d0 -f /tmp/file.mjpeg`.
Change `-d0` to any camera number you want to use from `/dev/video*`.

Convert the mjpeg file to mp4 by running `v4l2-command.sh -f /tmp/file.mjpeg -c /tmp/file.mp4`.

# TODO

- [x] Raw footage gekregen
- [x] getest of croppen op de Pi. (werkt niet)
- [x] testen op de Pi. (Werkt, opslag is niet snel genoeg. Ram wel)
- [x] interface in python gemaakt
- [x] logisch opslaan op de Pi
- [ ] Set persistent configuration with udev.
- [ ] Stream video over the internet

# Notes
https://linuxtv.org/wiki/index.php/V4L_capturing#Recommended_process

Storage troughput needed for
- Raw 2304x1536 (24 fps):
  140 - 170 MB / s
- Mjpeg 2304x1536 (48 fps)
  26 - 28 MB / s

For a 1 hour clip that means
- Raw 2304x1536 (24 fps):
  600 GB of storage
- Mjpeg 2304x1536 (48 fps)
  100 GB of storage
