import os
import smtplib, ssl


def send_email(offer_url:str, title:str, receiver_mail:str):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = os.getenv('GMAIL_USER')   # Enter your address
    password = os.getenv('GMAIL_PASSWORD')
    
    message = f"""\
    Subject: Potencjalne auto


    Tytuł oferty: {title}
    Link do oferty: {offer_url}

    Ta wiadomość została wygenerowana automatycznie. ~Bart
    """

    if len(send_email) == 0:
        raise Exception("Sender mail cannot be empty")

    if len(password) == 0:
        raise Exception("Sender password cannot be empty")

    if len(receiver_mail) == 0:
        raise Exception("Receiver mail cannot be empty")

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        
        server.sendmail(sender_email, receiver_email, message.encode("utf8"))

