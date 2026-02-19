from picamzero import Camera

def capture():
    cam = Camera()
    cam.take_photo("image.jpg") #save the image to your desktop
    return 0
