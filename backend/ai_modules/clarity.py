import cv2
import numpy as np
from PIL import Image

def studio_clarity(img: Image.Image):
    img = np.array(img)
    denoised = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    sharpened = cv2.addWeighted(denoised, 1.5, denoised, -0.5, 0)
    return Image.fromarray(sharpened)
