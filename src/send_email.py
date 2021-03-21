import os
import smtplib
import ssl


def send_email(offer_url: str, title: str, receiver_email: str, sender_email: str, sender_password: str):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    message = f"""Subject: Potential car

    
    
    Offer link: {offer_url}
    Take a look

    This message was generated automatically ~Bart
    """

    print(f"SENDING FROM {sender_email}, to {receiver_email} message:")
    print(message)

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_password)

        server.sendmail(sender_email, receiver_email, message.encode("utf8"))

    print("MESSAGE SENT")
