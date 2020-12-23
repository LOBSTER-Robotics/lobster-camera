# import the opencv library
import cv2

camera_number = 0

# define a video capture object
vid = cv2.VideoCapture(camera_number)

if vid.isOpened():
    print("Opening succeeded")
else:
    print("Could not open camera {}".format(camera_number))

# After the loop release the cap object
vid.release()
