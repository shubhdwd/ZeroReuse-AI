import cv2
import numpy as np
from PIL import Image

def black_white(img: Image.Image):
    img = np.array(img)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    bw = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    return Image.fromarray(bw)
