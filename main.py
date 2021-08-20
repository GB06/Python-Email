import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "Password"
subject = "Subject"
body = """
Body
"""

# header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logging in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent")

except smtplib.SMTPAuthenticationError:
    print("Error... Make sure you enable \"Less Secure App\" in Google Settings!)

