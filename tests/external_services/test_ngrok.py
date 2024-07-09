def test_ngrok():
    from app.external_services.service_ngrok import get_ngrok_url
    url = get_ngrok_url()
    assert type(url) == str