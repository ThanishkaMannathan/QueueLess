from flask import Flask, request, send_from_directory
from flask_cors import CORS
from twilio.rest import Client

app = Flask(__name__)
CORS(app)

# Home page
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# Static files (css/js)
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(".", path)

# SMS API
@app.route("/send", methods=["POST"])
def send_sms():
    phone = request.form["phone"]

    client = Client("YOUR_ACCOUNT_SID", "YOUR_AUTH_TOKEN")

    client.messages.create(
        body="🔔 QueueLess: It's your turn!",
        from_="YOUR_TWILIO_NUMBER",
        to=phone
    )

    return "SMS Sent"

if __name__ == "__main__":
    app.run()