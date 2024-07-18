import sys
import os

picdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
from PIL import Image, ImageDraw, ImageFont
import traceback

logging.basicConfig(level=logging.INFO)

def print_img(image):
    import epaper
    try:
        logging.info("Printing Text")
        epd = epaper.epaper('epd2in7').EPD()

        '''2Gray(Black and white) display'''
        logging.info("init and Clear")
        epd.init()
        epd.Clear(0xFF)

        epd.display(epd.getbuffer(image))
        time.sleep(2)

        logging.info("Goto Sleep...")
        epd.sleep()

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epaper.epaper('epd2in7').epdconfig.module_exit()
        exit()
    return {'status': 200}

def clear_screen():
    try:
        logging.info("Printing Text")
        epd = epaper.epaper('epd2in7').EPD()

        '''2Gray(Black and white) display'''
        logging.info("init and Clear")
        epd.init()
        epd.Clear(0xFF)
    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epaper.epaper('epd2in7').epdconfig.module_exit()
        exit()