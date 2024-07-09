from ..utils.txt_format import wrap_text
from ..display.build_images import build_img_from_text

def text_to_image(msg, font='arial'):
    wrapped_txt = wrap_text(msg)
    img = build_img_from_text(wrapped_txt, font)
    return img