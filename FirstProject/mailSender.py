import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password"
subject = "python"
body = "test python mail ."

message = f"""From: {sender}
To: {receiver}
Subject: {subject} \n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("logged in: ..")

    server.sendmail(sender,receiver,message)
    print("Message has sent;")
except smtplib.SMTPAuthenticationError:
    print("Incorrect password")