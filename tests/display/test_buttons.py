from tests.conftest import is_rpi
import pytest


@pytest.mark.skipif(
    True,
    reason="Only used for manual execution of the test for button testing"
)
def test_buttons():
    import threading
    from app.display.buttons import button_listen
    button_listen = threading.Thread(target=button_listen)
    button_listen.start()
    assert True
