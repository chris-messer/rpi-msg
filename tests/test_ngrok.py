import pytest

def test_ngrok():
    from utils.establish_ngrok import get_ngrok_url
    url = get_ngrok_url()
    assert type(url) == str