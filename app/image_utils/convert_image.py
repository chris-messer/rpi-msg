from PIL import Image
import numpy as np
from app.utils.utils import get_project_root


def convert_image_to_bmp(img):
    img_gray = img.convert('L')
    return img_gray
