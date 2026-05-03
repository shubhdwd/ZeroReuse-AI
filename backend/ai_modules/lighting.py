import cv2
import numpy as np
from PIL import Image

def dramatic_lighting(img: Image.Image):
    img = np.array(img)
    img = cv2.convertScaleAbs(img, alpha=1.6, beta=-40)
    return Image.fromarray(img)

def cinematic_lighting(img: Image.Image):
    img = np.array(img)
    img = cv2.convertScaleAbs(img, alpha=1.3, beta=10)

    h, w = img.shape[:2]
    bar = int(h * 0.1)
    img[:bar, :] = 0
    img[h-bar:, :] = 0

    return Image.fromarray(img)
