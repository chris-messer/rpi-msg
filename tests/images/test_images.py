from PIL import Image

def test_save_image(img_url, tmp_out_dir):
    from app.image_utils.save_image import save_image_from_url
    import os

    save_image_from_url(img_url, tmp_out_dir, 'image.png')
    assert os.path.exists(f'{tmp_out_dir}/image.png')

def test_convert_image(tmp_image, tmp_out_dir):
    from app.image_utils.convert_image import convert_image_to_bmp
    import os

    img_converted = convert_image_to_bmp(tmp_image)
    img_converted.save(f'{tmp_out_dir}/converted_image.bmp')

    assert os.path.isfile(f'{tmp_out_dir}/converted_image.bmp')

def test_crop_image(tmp_image):
    from app.image_utils.crop_image import crop_image

    cropped_img = crop_image(tmp_image, 264, 176)
    assert cropped_img.size == (264, 176)

def test_scale_image(tmp_image):
    from app.image_utils.scale_image import scale_image

    scaled_img = scale_image(tmp_image, 264)
    assert scaled_img.size[0] == 264

def test_transform(img_url):
    from app.image_utils.transform_image import get_and_transform_image

    img = get_and_transform_image(img_url)
    assert True