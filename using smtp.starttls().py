# using smtp.starttls() 

import smtplib, ssl

host = 'smtp.gmail.com'
port = 465

username = 'aoen143@gmail.com'
password = input("Enter you password: ")


from_email = username
to_email = 'aoen143@gmail.com'

# securing connection
context = ssl.create_default_context()

with smtplib.SMTP(host, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(username , password)
    server.sendmail(sender_email, receiver_email, message)
    
