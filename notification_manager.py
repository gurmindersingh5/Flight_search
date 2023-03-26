from twilio.rest import Client
import smtplib
TWILIO_SID = "sid here"
TWILIO_AUTH_TOKEN = "6745c3ce******079d78d3"
TWILIO_VIRTUAL_NUMBER = "+1507620****"
TWILIO_VERIFIED_NUMBER = "+1437*******"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "my email here"
MY_PASSWORD = "app passwrd here"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, message, google_flight_link, emails="send_to_email@yahoo.com"):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            # for email in emails:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=emails,
                msg=f"{message}".encode('utf-8')
                )
            print(message)