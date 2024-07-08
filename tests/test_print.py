import pytest


def test_print():
    from utils.build_images import plain_text
    from utils.print_to_eink import print_text, clear_screen

    t = plain_text('Hello World', 'love')
    print_text(t)

def test_clear():
    from utils.print_to_eink import clear_screen
    clear_screen()

def test_ngrok():
    from utils.establish_ngrok import get_ngrok_url
    url = get_ngrok_url()
    assert type(url) == str