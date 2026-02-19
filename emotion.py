import face_recognition_models

image = face_recognition.load_image_file("image.jpg")
face_locations = face_recognition_model_location(image)

print(face_locations)

# face_locations is now an array listing the co-ordinates of each face!
