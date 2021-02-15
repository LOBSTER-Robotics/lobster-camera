import time
import subprocess
timestr = time.strftime("%d-%m-%Y_%H:%M:%S")
print(timestr)

filename = timestr + ".mjpeg"

camera_device = 0

subprocess.run(["./v4l-command.sh", "-d", str(camera_device), "-f", filename])
