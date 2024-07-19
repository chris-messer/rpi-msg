from PIL import Image


def scale_image (img, pixel_width):
    wpercent = (pixel_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((pixel_width, hsize), Image.Resampling.LANCZOS)
    return img