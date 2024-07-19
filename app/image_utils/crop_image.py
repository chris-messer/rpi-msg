from PIL import Image


def crop_image(img, pixel_width, pixel_height):

    # Calculate the crop size in pixels
    crop_width = int(pixel_width)
    crop_height = int(pixel_height)

    # Get the dimensions of the original image
    width, height = img.size

    # Calculate the position to start the crop to center it
    left = (width - crop_width) // 2
    top = (height - crop_height) // 2
    right = (width + crop_width) // 2
    bottom = (height + crop_height) // 2

    # Crop the image
    img_cropped = img.crop((left, top, right, bottom))
    return img_cropped
