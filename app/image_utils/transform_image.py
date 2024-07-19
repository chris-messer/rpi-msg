from PIL import Image
from io import BytesIO

import requests
from app.image_utils.scale_image import scale_image
from app.image_utils.crop_image import crop_image
from app.image_utils.convert_image import convert_image_to_bmp

def get_and_transform_image(url):
    img = Image.open(BytesIO(requests.get(url).content))
    scaled = scale_image(img, 264)
    cropped = crop_image(scaled, 264, 176)
    converted = convert_image_to_bmp(cropped)
    return converted
