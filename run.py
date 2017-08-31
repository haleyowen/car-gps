import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def response():

    body = request.values.get('Body', None)
    print body

    send_message_to_gps()
    return get_response("Hello, Mobile Monkey")

def get_response(message):
    return '<?xml version="1.0" encoding="UTF-8"?><Response><Message>' + message + '</Message></Response>'
    
def send_message_to_gps():
    account_sid = ""
    auth_token = ""

    client = Client(account_sid, auth_token)

    message = client.messages.create(to="", from_="", body="GPS#")
    print 'message: ' + str(message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
