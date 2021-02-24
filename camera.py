import time
import signal
import subprocess
import os
import logging

def get_timestamped_filename(extension):
    timestr = time.strftime("%d-%m-%Y_%H:%M:%S")
    filename = timestr + "." + extension
    return filename


class Camera:
    file_location = ""
    filename = ""
    recording = False
    camera_device = "0" # File location of the camera: /dev/video*
    directory = ""

    def __init__(self, frame_width, frame_height, videocodec):
        #WIDTH_HEIGHT_PF="width=2304,height=1536,pixelformat=MJPG"
        WIDTH_HEIGHT_PF="width={},height={},pixelformat={}".format(frame_width, frame_height, videocodec)
        subprocess.run(["v4l2-ctl", "-d", self.camera_device, "-v", WIDTH_HEIGHT_PF]) # TODO do error handling with return value

    def start_recording(self):
        self.directory = os.path.join('/tmp', "recordings");
        self.filename = get_timestamped_filename("mjpeg");
        file_location = os.path.join(self.directory, self.filename);
        os.makedirs(self.directory, exist_ok=True) # create the recordings directory and all directories above it

        # start the recording process
        self.process = subprocess.Popen(["v4l2-ctl", "-d", self.camera_device, "--stream-user", "--stream-to", self.filename],
                shell = False
                )

    def is_recording(self):
        return not p.poll()

    def stop_recording(self):
        self.process.terminate()
        self.process.wait()

    def get_file_location(self):
        return file_location


c = Camera(2304, 1536, "MJPG")
c.start_recording()
print("recording")
time.sleep(3)
c.stop_recording()
