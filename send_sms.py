from twilio.rest import TwilioRestClient

def send_message(recipient_number, message):
    account_sid = "ACea9ef94f5cb0de44363955e9f4c70390"
    auth_token = "f00563727f5d0be1fba12225026c5668"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to=recipient_number,
                                     from_="+19253266132",
                                     body=message)
