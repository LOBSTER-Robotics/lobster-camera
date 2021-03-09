import time
import signal
import subprocess
import os
import logging

def get_timestamped_filename(extension):
    timestr = time.strftime("%d-%m-%Y_%H-%M-%S")
    filename = timestr + "." + extension
    return filename


class Camera:
    file_location = ""
    filename = ""
    recording = False
    camera_device = "0" # File location of the camera: /dev/video*
    directory = "/media/pi/Video_storage/recordings"

    def __init__(self, frame_width, frame_height, videocodec):
        #WIDTH_HEIGHT_PF="width=2304,height=1536,pixelformat=MJPG"
        WIDTH_HEIGHT_PF="width={},height={},pixelformat={}".format(frame_width, frame_height, videocodec)
        subprocess.run(["v4l2-ctl", "-d", self.camera_device, "-v", WIDTH_HEIGHT_PF]) # TODO do error handling with return value

    def start_recording(self):
        self.filename = get_timestamped_filename("mjpeg"); # TODO change this to raw when recording raw footage
        self.file_location = os.path.join(self.directory, self.filename);
        print ("Saving file to {}".format(self.file_location))
        os.makedirs(self.directory, exist_ok=True) # create the recordings directory and all directories above it

        # start the recording process
        self.process = subprocess.Popen(["v4l2-ctl", "-d", self.camera_device, "--stream-user", "--stream-to", self.file_location],
                shell = False
                )

    def is_recording(self):
        return not self.process.poll()

    def stop_recording(self):
        self.process.terminate()
        self.process.wait()

    def get_file_location(self):
        return self.file_location


c = Camera(2304, 1536, "MJPG")
while True:
    c.start_recording()
    time.sleep(1000)
    print("restarting")
    c.stop_recording()
print("done")
