from gpiozero import Button
from app.display.print_to_eink import clear_screen
from app.messaging.messages import send_message
from dotenv import load_dotenv
import logging
from time import gmtime, strftime



logging.basicConfig(level=logging.INFO)
load_dotenv()

btn1 = Button(5)
btn2 = Button(6)
btn3 = Button(13)
btn4 = Button(19)


def key1():
    ts = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    send_message('18179956114',f'Kali saw your image at {ts}')
    send_message('18175019724',f'Kali saw your image at {ts}')

def key2():
    clear_screen()


def button_listen():
    btn1.when_pressed = key1
    btn2.when_pressed = key2
