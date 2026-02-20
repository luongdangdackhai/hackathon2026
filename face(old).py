

    # importing the cv2 library
import cv2
import subprocess
import time
from picamzero import Camera

def capture():
    cam = Camera()
    #pic = cam.capture_array() #save the image to your desktop
    pic =0
    cam.take_photo("image.jpg")
    #process = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #process.communicate(input="scp image.jpg sham@10.78.19.181:/home/sham/Desktop/hackathonproject2026")
    #print("image sent")

    return pic


def locate(pic):
    # loading the haar case algorithm file into alg variable
    alg = "haarcascade_frontalface_default.xml"
    # passing the algorithm to OpenCV
    haar_cascade = cv2.CascadeClassifier(alg)
    # loading the image path into file_name variable - replace <INSERT YOUR IMAGE NAME HERE> with the path to your image
   #file_name = "image.jpg"
    # reading the image
    img = cv2.imread("image.jpg", 0)
    # creating a black and white version of the image
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # detecting the faces
    faces = haar_cascade.detectMultiScale(
        gray_img, scaleFactor=1.05, minNeighbors=2, minSize=(100, 100)
    )
    #print(faces)
    return faces

'''
i = 0
# for each face detected
for x, y, w, h in faces:
    # crop the image to select only the face
    cropped_image = img[y : y + h, x : x + w]
    pos = img[y:y+100, x: x+100]
    # loading the target image path into target_file_name variable  - replace <INSERT YOUR TARGET IMAGE NAME HERE> with the path to your target image
    target_file_name = 'stored-faces/' + str(i) + '.jpg'
    cv2.imwrite(
        target_file_name,
        cropped_image,
    )
    cv2.imwrite('pos.jpg',pos)
    i = i + 1;
'''
while True:
    pic = capture()
    
    print(locate(pic))
    
