

def crop_image(img):
    img = Image.open(image_path)

    # Calculate the crop size in pixels
    crop_width = int(crop_width_inches * dpi)
    crop_height = int(crop_height_inches * dpi)

    # Get the dimensions of the original image
    width, height = img.size

    # Calculate the position to start the crop to center it
    left = (width - crop_width) // 2
    top = (height - crop_height) // 2
    right = (width + crop_width) // 2
    bottom = (height + crop_height) // 2

    # Crop the image
    img_cropped = img.crop((left, top, right, bottom))

    # Return the cropped image
    return img_cropped