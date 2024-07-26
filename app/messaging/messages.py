from app.external_services.service_twilio import get_client


def send_message(number, message):
    client = get_client()
    message = client.messages.create(
        body=message,
        from_="+18336811158",
        to=number)
    return message