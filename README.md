# Lobster-camera
This is the camera recording software for the lobster robot. It uses v4l2-ctl to
record the camera. It will be optimized for running on a raspberry pi 4 with a
usb 3.0 v4l2 camera.

# Installation

## required packages (Ubuntu):
- python3
- v4l2-utils

You will also need a POSIX shell

You can now test if it works by running `tests/v4l2-command.sh` or
`tests/v4l2-raw-command.sh`.

# TODO

- [ ] Raw footage gekregen
- [ ] interface in python gemaakt
- [ ] logisch opslaan op de Pi
- [ ] getest of croppen op de Pi.
- [ ] testen op de Pi
- [ ] Set persistent configuration with udev.
- [ ] Stream video over the internet

# Notes
https://linuxtv.org/wiki/index.php/V4L_capturing#Recommended_process
