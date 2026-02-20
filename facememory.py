

    # importing the cv2 library
import cv2
import subprocess
import time
import os
from picamzero import Camera

def capture():
    cam = Camera()

#save to memory method (slower)
    cam.take_photo("image.jpg")

#debug code
    #process = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #process.communicate(input="scp image.jpg sham@10.78.19.181:/home/sham/Desktop/hackathonproject2026")
    #print("image sent")

    return 0


def locate():
    # loading the haar case algorithm file into alg variable
    alg = "haarcascade_frontalface_default.xml"
    # passing the algorithm to OpenCV
    haar_cascade = cv2.CascadeClassifier(alg)
    # loading the image path into file_name variable - replace <INSERT YOUR IMAGE NAME HERE> with the path to your image
    # reading the image
    img = cv2.imread("image.jpg", 0)
    # creating a black and white version of the image
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # detecting the faces
    faces = haar_cascade.detectMultiScale(
        gray_img, scaleFactor=1.05, minNeighbors=2, minSize=(300, 300)
    )
    #storeface(faces,img)
    #print(faces)
 #   process = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  #  process.communicate(input="scp image.jpg sham@10.78.19.181:/home/sham/Desktop/hackathonproject2026 \n")
   # print("image sent")

    
    return faces

def storeface(faces,img):
    i = 0
    # for each face detected
    for x, y, w, h in faces:
        # crop the image to select only the face
        cropped_image = img[y : y + h, x : x + w]
        pos = img[y:y+100, x: x+100]
        # loading the target image path into target_file_name variable  - replace <INSERT YOUR TARGET IMAGE NAME HERE> with the path to your target image
 #       target_file_name = '~/stored-faces/' + str(i) + '.jpg'
        target_file_name = os.path.join('stored-faces', str(i)+'.jpg')
        cv2.imwrite(
            target_file_name,
            cropped_image,
        )

        process = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.communicate(input="scp ~/stored-faces/"+str(i)+'.jpg'+" sham@10.78.19.181:/home/sham/Desktop/hackathonproject2026 \n")
        print(str(i),"sent")
        
        i = i + 1;



while True:
    start_time = time.perf_counter()

    capture()
    print(locate())

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    print(f"Elapsed wall-clock time: {elapsed_time:.4f} seconds")
  
   
    

