import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse, Message

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = MessagingResponse().message("Hello, Mobile Monkey")
    return "<?xml version="1.0" encoding="UTF-8"?><Response><Message>Hello, Mobile Monkey</Message></Response>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
