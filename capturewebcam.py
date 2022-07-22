import time
import cv2
from cv2 import VideoCapture, VideoWriter_fourcc, VideoWriter
print('packages imported')

flag_debug = 0
SUBJ_ID = 123 #PARAMS.subject_code
SESSION_NAME = 'test' #PARAMS.session.name

print('const variables declared')

def capturewebcam(command):
    capture = VideoCapture(0)
    video_code = VideoWriter_fourcc(*'MPEG')
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    output = VideoWriter(f'vismodR01/helper_scripts/sub-{SUBJ_ID}_task-{SESSION_NAME}_webcam.avi', video_code, fps, (width, height))     
    # open preview window
    if flag_debug:
        ret,frame = capture.read()
        cv2.imshow("Debug Camera Test", frame)
        cv2.waitKey(5000)
    print('camera init')
    # create video capture object to capture the video from our webcam
    #if command == 'Initialize':
        #capture = VideoCapture(0)
        #video_code = VideoWriter_fourcc(*'MPEG')
        #width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        #height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #fps = int(capture.get(cv2.CAP_PROP_FPS))
        #output = VideoWriter(f'vismodR01/helper_scripts/sub-{SUBJ_ID}_task-{SESSION_NAME}_webcam.avi', video_code, fps, (width, height))     
        # open preview window
        #if flag_debug:
            #ret,frame = capture.read()
            #cv2.imshow("Debug Camera Test", frame)
            #cv2.waitKey(5000)
    print('camera recording')
    if command == 'StartRecording':
        while(True):
            # Capture each frame of webcam video
            ret,frame = capture.read()
            #cv2.imshow("My cam video", frame)
            output.write(frame)
            if flag_debug:
            # Close and break the loop after pressing "x" key (debug purposes)
                if cv2.waitKey(1) &0XFF == ord('x'):
                    break
    
    if command == 'StopRecording':
        print('recording stopped')
        # close the already opened camera
        capture.release()
        # close the already opened file
        output.release()
        # close the window and de-allocate anay asssociated memory usage
        cv2.destroyAllWindows()

    if command == 'Properties':
        print("CAP_PROP_FPS : '{}'".format(capture.get(cv2.CAP_PROP_FPS)))
        print("CAP_PROP_POS_MSEC : '{}'".format(capture.get(cv2.CAP_PROP_POS_MSEC)))
        print("CAP_PROP_FRAME_COUNT  : '{}'".format(capture.get(cv2.CAP_PROP_FRAME_COUNT)))
        print("CAP_PROP_BRIGHTNESS : '{}'".format(capture.get(cv2.CAP_PROP_BRIGHTNESS)))
        print("CAP_PROP_CONTRAST : '{}'".format(capture.get(cv2.CAP_PROP_CONTRAST)))
        print("CAP_PROP_SATURATION : '{}'".format(capture.get(cv2.CAP_PROP_SATURATION)))
        print("CAP_PROP_HUE : '{}'".format(capture.get(cv2.CAP_PROP_HUE)))
        print("CAP_PROP_GAIN  : '{}'".format(capture.get(cv2.CAP_PROP_GAIN)))
        print("CAP_PROP_CONVERT_RGB : '{}'".format(capture.get(cv2.CAP_PROP_CONVERT_RGB)))

    return output

#init = capturewebcam('Initialize')
capturewebcam('StartRecording')
capturewebcam('StopRecording')
capturewebcam('Properties')
print('video captured and saved')