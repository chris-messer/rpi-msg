import platform
import pytest


def is_rpi():
    if platform.machine() == 'armv7l':
        return True
    else:
        return False

