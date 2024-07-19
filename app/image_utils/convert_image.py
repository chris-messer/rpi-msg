from PIL import Image
import numpy as np
from app.utils.utils import get_project_root

def convert_image_to_bmp(in_path, out_path):

    img = Image.open(f'{in_path}/image.png')
    ary = np.array(img)

    # Split the three channels
    r,g,b = np.split(ary,3,axis=2)
    r=r.reshape(-1)
    g=r.reshape(-1)
    b=r.reshape(-1)

    # Standard RGB to grayscale
    bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2],
    zip(r,g,b)))
    bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
    bitmap = np.dot((bitmap > 128).astype(float),255)
    # inv_mitmap = np.dot((bitmap < 128).astype(float),255)
    im = Image.fromarray(bitmap.astype(np.uint8))
    im.save(f'{out_path}/image.bmp')