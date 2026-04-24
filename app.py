from flask import Flask, request
from flask_cors import CORS
from twilio.rest import Client

app = Flask(__name__)
CORS(app)

# 🔑 YOUR TWILIO DETAILS
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
twilio_number = "+15754194812"

client = Client(account_sid, auth_token)

@app.route('/send', methods=['POST'])
def send_sms():
    phone = request.form['phone']

    # Ensure + format
    if not phone.startswith("+"):
        phone = "+" + phone

    print("Sending SMS to:", phone)

    client.messages.create(
        body="🔔 QueueLess: It's your turn!",
        from_=twilio_number,
        to=phone
    )

    return "Message Sent"

if __name__ == "__main__":
    app.run(debug=True)