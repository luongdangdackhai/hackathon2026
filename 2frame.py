




    # importing the cv2 library
import cv2
import subprocess
import time
import os
import numpy as np
# Set before importing picamera2 or initiating Picamera2()
os.environ['LIBCAMERA_LOG_LEVELS'] = '4' 
#from picamzero import Camera
from picamera2 import Picamera2



def capture(cam):

    pic = cam.capture_array("main")
    time.sleep(0.000001)
    print("captured")

    '''
    request = cam.capture_request(flush=True)
    print("start request")
# Extract data from the 'main' buffer
    pic = request.make_array('main') 
    print("capture array")
    request.flush()
    print("flush")
# Release the request back to the system
    cam.release_request(request)
    print("release request")
    '''
    #pic = increase_brightness_hsv(pic,50)
#debug code
    #process = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #process.communicate(input="scp image.jpg sham@10.78.19.181:/home/sham/Desktop/hackathonproject2026")
    #print("image sent")


    
 #   pic = np.delete(pic, 3, axis=2)    
  #  cv2.imwrite("image.jpg", pic)

    #print(pic)
    return pic



def sendphoto(pic,num):
    cv2.imwrite("image"+str(num)+".jpg", pic)
    process = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.communicate(input="scp image"+str(num)+".jpg sham@10.51.165.181:/home/sham/Desktop/hackathonproject2026 \n \\")
    print(str(num)+"image sent")






try:
    cam = Picamera2()
    print("initilized cam")
    preview_config = cam.create_still_configuration(main={"size": cam.sensor_resolution})
    print("create preview config")
    cam.configure(preview_config)    
    print("configure config")

#save to memory method (faster)    
    cam.start()
    print("camstart")
    while True:
        start_time = time.perf_counter()

        sendphoto(capture(cam),1)
        sendphoto(capture(cam),2)
        

        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Elapsed wall-clock time: {elapsed_time:.4f} seconds")
except KeyboardInterrupt:
    cam.close()
    print("camclose")
