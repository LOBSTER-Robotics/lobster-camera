import time
import subprocess
import os


timestr = time.strftime("%d-%m-%Y_%H:%M:%S")
print(timestr)

filename = timestr + ".mjpeg"

directory = os.path.join('/tmp', "recordings");
location = os.path.join(directory, filename);

os.makedirs(directory, exist_ok=True)

camera_device = 0

subprocess.run(["./v4l-command.sh", "-d", str(camera_device), "-f", location])
