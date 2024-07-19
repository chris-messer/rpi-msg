import requests
from app.utils.utils import get_project_root

def save_image_from_url(url, out_path, file_name):
    root = get_project_root()
    with open(f'{out_path}/{file_name}', 'wb') as f:
        f.write(requests.get(url).content)
