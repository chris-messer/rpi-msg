import pytest
from tests.conftest import is_rpi
@pytest.mark.skipif(
    not is_rpi(),
    reason="requires host system to have display"
)
def test_print():
    from app.display.build_images import build_img_from_text
    from app.display.print_to_eink import print_img

    t = build_img_from_text('Hello World', 'love')
    print_img(t)


@pytest.mark.skipif(
    not is_rpi(),
    reason="requires host system to have display"
)
def test_clear():
    from app.display.print_to_eink import clear_screen
    clear_screen()


@pytest.mark.skipif(
    not is_rpi(),
    reason="requires host system to have display"
)
def test_build_image():
    from app.display.build_images import build_img_from_text
    img = build_img_from_text('Hello there!')
    img.show()