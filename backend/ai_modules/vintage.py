import cv2
import numpy as np
from PIL import Image

def vintage_filter(img: Image.Image):
    img = np.array(img)

    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])

    sepia = cv2.transform(img, kernel)
    sepia = np.clip(sepia, 0, 255)

    return Image.fromarray(sepia.astype(np.uint8))
