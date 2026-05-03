import cv2
import numpy as np
from PIL import Image

def blur_face(img: Image.Image) -> Image.Image:
    # Convert PIL image to OpenCV format
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Load the Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Convert to grayscale for detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Blur each detected face
    for (x, y, w, h) in faces:
        # Extract the face region
        face_roi = img[y:y+h, x:x+w]
        # Apply strong Gaussian blur to the face region
        blurred_face = cv2.GaussianBlur(face_roi, (31, 31), 0)
        # Replace the original face with the blurred one
        img[y:y+h, x:x+w] = blurred_face
    
    # Convert back to PIL format
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return Image.fromarray(img)