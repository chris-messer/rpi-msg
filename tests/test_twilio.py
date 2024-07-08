import pytest


def test_twilio():
    from utils.set_twilio_hook import set_webhook_address
    from twilio.rest import Client
    import os

    url = 'https://demo.twilio.com/welcome/messaging/'

    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    set_webhook_address(url)

    response = client.incoming_phone_numbers(
        os.environ["TWILIO_PHONE_SID"]
    ).fetch()

    assert url == response.sms_url