from PIL import Image

def test_save_image():
    from app.image_utils.save_image import save_image_from_url
    from app.utils.utils import get_project_root
    root = get_project_root()
    import os
    save_image_from_url\
        ('https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187.jpg?w=718&h=479')


    assert os.path.exists(f'{root}/images/raw/image.png')

def test_convert_image(tmp_path):
    from app.image_utils.convert_image import convert_image_to_bmp
    from app.utils.utils import get_project_root
    from app.image_utils.save_image import save_image_from_url
    import os

    temp_in_dir = tmp_path / "raw"
    temp_in_dir.mkdir()

    temp_out_dir = tmp_path / "bmp"
    temp_out_dir.mkdir()

    save_image_from_url(
        'https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187.jpg?w=718&h=479',
        f'{temp_in_dir}',
        'image.png'
    )

    convert_image_to_bmp(temp_in_dir, temp_out_dir)
    assert os.path.isfile(f'{temp_out_dir}\\image.bmp')
