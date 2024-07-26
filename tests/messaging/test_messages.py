def test_send_message():
    from app.messaging.messages import send_message
    message = send_message('18179956114', 'Test Passed!')
    assert message.error_code is None