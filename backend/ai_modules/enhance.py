import cv2
import numpy as np
from PIL import Image

def enhance_image(img):
    img_np = np.array(img)
    enhanced = cv2.detailEnhance(img_np, sigma_s=10, sigma_r=0.15)
    return Image.fromarray(enhanced)
