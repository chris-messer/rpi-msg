import pytest


@pytest.fixture
def img_url():
    return 'https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187.jpg?w=718&h=479'


@pytest.fixture
def tmp_in_dir(tmp_path):
    temp_in_dir = tmp_path / "in"
    temp_in_dir.mkdir()
    return temp_in_dir


@pytest.fixture
def tmp_out_dir(tmp_path):
    temp_out_dir = tmp_path / "out"
    temp_out_dir.mkdir()
    return temp_out_dir

@pytest.fixture
def tmp_image(tmp_in_dir):
    from app.image_utils.save_image import save_image_from_url
    from PIL import Image
    save_image_from_url(
        'https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187.jpg?w=718&h=479',
        f'{tmp_in_dir}',
        'image.png'
    )
    return Image.open(f'{tmp_in_dir}/image.png')