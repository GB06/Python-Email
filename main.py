import smtplib

sender = "Sender_Email@gmail.com"
receiver = "Receiver_Email@gmail.com"
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
    print("Done!")

except smtplib.SMTPAuthenticationError:
    print("Error")

