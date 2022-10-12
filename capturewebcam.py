import os

import cv2
import pandas as pd
from cv2 import VideoCapture, VideoWriter, VideoWriter_fourcc, waitKey

params = pd.read_csv('C:/Users/feusn/Desktop/vismodR01/parameters.csv')

FLAG_DEBUG = 1 #int(params['flag_debug'])
SUBJ_ID = params['subject_code'][0]
SESSION_NAME = params['session_name'][0]


# This will return video from the first webcam on your computer.
capture = VideoCapture(0)

# Variables to create videowriter object
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = fps = int(capture.get(cv2.CAP_PROP_FPS))
vidpath = f'C:/Users/feusn/Desktop/vismodR01/sub-{SUBJ_ID}_task_{SESSION_NAME}_webcam.avi'

# Define the codec and create VideoWriter object
fourcc = VideoWriter_fourcc(*'XVID')
output = VideoWriter(vidpath, fourcc, fps, (width, height))

# loop runs if capturing has been initialized.
while(True):
    # Capture each frame of webcam video
    # ret checks return at each frame
    ret,frame = capture.read()
    
    # output the frame
    output.write(frame)
    
    # input frame is shown in the window
    cv2.imshow("webcam video", frame)

    # Close and break the loop after pressing "x" key
    if cv2.waitKey(1) &0XFF == ord('x'):
        break

# close the already opened camera
capture.release()
# close the already opened file
output.release()
# close the window and de-allocate anay asssociated memory usage
cv2.destroyAllWindows()

#if FLAG_DEBUG == 1:
    #print("FPS : '{}'".format(capture.get(cv2.CAP_PROP_FPS)))
    #print("POS_MSEC : '{}'".format(capture.get(cv2.CAP_PROP_POS_MSEC)))
    #print("FRAME_COUNT  : '{}'".format(capture.get(cv2.CAP_PROP_FRAME_COUNT)))
    #print("BRIGHTNESS : '{}'".format(capture.get(cv2.CAP_PROP_BRIGHTNESS)))
    #print("CONTRAST : '{}'".format(capture.get(cv2.CAP_PROP_CONTRAST)))
    #print("SATURATION : '{}'".format(capture.get(cv2.CAP_PROP_SATURATION)))
    #print("HUE : '{}'".format(capture.get(cv2.CAP_PROP_HUE)))
