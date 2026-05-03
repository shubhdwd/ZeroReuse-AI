import cv2
import numpy as np
from PIL import Image

def cyberpunk_cv(img: Image.Image):
    img = np.array(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    hsv[...,1] = cv2.add(hsv[...,1], 60)   # saturation
    hsv[...,2] = cv2.add(hsv[...,2], 40)   # brightness

    neon = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    return Image.fromarray(neon)
