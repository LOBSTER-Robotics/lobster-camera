# import the opencv library 
import cv2 

# define a video capture object 
vid = cv2.VideoCapture(4) 

width= int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer= cv2.VideoWriter('basicvideo.mjpeg', cv2.VideoWriter_fourcc(*'MJPG'), 48, (width,height))

while(True): 

    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 

    writer.write(frame)

    # Display the resulting frame 
    cv2.imshow('frame', frame) 

    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
