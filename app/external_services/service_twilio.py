import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

def set_webhook_address(url: str):
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    incoming_phone_number = client.incoming_phone_numbers(
        os.environ["TWILIO_PHONE_SID"]
    ).update(sms_url=url)

def get_client():
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    return client

if __name__ == '__main__':
    set_webhook_address('https://demo.twilio.com/welcome/messaging/')