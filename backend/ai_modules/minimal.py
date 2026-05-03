import cv2
import numpy as np
from PIL import Image

def minimal_aesthetic(img: Image.Image):
    img = np.array(img)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    final = cv2.convertScaleAbs(gray, alpha=1.2, beta=10)
    return Image.fromarray(final)
