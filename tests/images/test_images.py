
def test_save_image():
    from app.image_utils.save_image import save_image_from_url
    from app.utils.utils import get_project_root
    root = get_project_root()
    import os
    save_image_from_url\
        ('https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187.jpg?w=718&h=479')


    assert os.path.exists(f'{root}/images/raw/image.png')

def test_convert_image():
    from app.image_utils.convert_image import convert_image_to_bmp
    convert_image_to_bmp()
    assert True