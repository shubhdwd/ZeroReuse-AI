import cv2
import numpy as np
from PIL import Image

def soft_portrait(img: Image.Image):
    img = np.array(img)
    blur = cv2.GaussianBlur(img, (15, 15), 0)
    soft = cv2.addWeighted(img, 0.7, blur, 0.3, 0)
    return Image.fromarray(soft)
