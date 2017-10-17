from twilio.rest import Client

def send_message(recipient_number, message):
    account_sid = "account_sid"
    auth_token = "auth_token"
    client = Client(account_sid, auth_token)

    message = client.messages.create(to=recipient_number,
                                     from_="phone number",
                                     body=message)
