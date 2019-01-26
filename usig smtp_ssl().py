
import smtplib,ssl


host = 'smtp.gmail.com'
port = 587

username = input("Please Enter sender address: ")
password = input("Please Input password: ")

from_email = username
to_email  = ['aoen143@gmail.com']

# creating secured connection with ssl()
context = ssl.create_default_context()

with smtplib.SMTP(host, port, context) as server:
    server.login(username , password)
    server.sendmail(from_emal, to_email, 'Hello ! testing')
    
