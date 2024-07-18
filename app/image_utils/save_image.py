import requests
from app.utils.utils import get_project_root

def save_image_from_url(url):
    root = get_project_root()
    with open(f'{root}/images/raw/image.png', 'wb') as f:
        f.write(requests.get(url).content)
