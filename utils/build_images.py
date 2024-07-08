from PIL import Image, ImageDraw, ImageFont
import logging
import textwrap
import os
from utils.utils import get_project_root
root = get_project_root()

logging.basicConfig(level=logging.INFO)


def plain_text(_text, font):
    out = Image.new("RGB", (264, 176), (255, 255, 255))
    fnt = ImageFont.truetype(f"{str(root)}/fonts/{font}.ttf", 18)
    d = ImageDraw.Draw(out)

    d.multiline_text((10, 10), _text, font=fnt, fill=(0, 0, 0), spacing=6)

    #out.show()
    return out

def build_budget_text(budget_dict):
    wbr = round(budget_dict['remaining_weekly_budget'], 2)
    cur_bal = round(budget_dict['current_balance'], 2)
    last_purchase = budget_dict['last_purchase']['Vendor']
    last_purchase_amt = budget_dict['last_purchase']['Amount']
    _text = f"Weekly Remaining:   ${wbr}\n" \
            f"Current Balance:        ${cur_bal}\n\n" \
            f"{last_purchase}\n" \
            f"{last_purchase_amt}"
    return _text


