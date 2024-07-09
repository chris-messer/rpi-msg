def test_print():
    from app.display.build_images import build_img_from_text
    from app.display.print_to_eink import print_img

    t = build_img_from_text('Hello World', 'love')
    print_img(t)

def test_clear():
    from app.display.print_to_eink import clear_screen
    clear_screen()

