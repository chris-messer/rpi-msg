from PIL import Image, ImageDraw, ImageFont
import logging
from ..utils.utils import get_project_root
root = get_project_root()

logging.basicConfig(level=logging.INFO)


def build_img_from_text(_text, font):
    out = Image.new("RGB", (264, 176), (255, 255, 255))
    fnt = ImageFont.truetype(f"{str(root)}/fonts/{font}.ttf", 18)
    d = ImageDraw.Draw(out)

    d.multiline_text((10, 10), _text, font=fnt, fill=(0, 0, 0), spacing=6)

    #out.show()
    return out


