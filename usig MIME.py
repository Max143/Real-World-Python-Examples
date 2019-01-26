import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = input("Enter sender's email address: ")
receiver_email = input("Enter recipient email address: ")
password = input("Type your password and press enter: ")


message = MIMEMultipart('alternative')
message['Subject'] = sender_email
message['From'] = receiver_email
message['To'] = password


# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
python docs has many great tutorials:
www.abc.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.abc.com">Python Docs</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# convertin into MIMETEXT object

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# attaching object with MIMEMultipart

message.attach(part1)
message.attach(part2)

# Creating server now
host = 'smtp.gmail.com'
port = 587

# securing connection
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email)

    
