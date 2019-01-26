import smtplib

# setting up server first
host = "smtp.gmail.com"
port = 587

# declarnig sender's credential
username = "aoen143@gmail.com"
password = "mypasswordhere"

# recipient's email addresds
from_email = username
to_list = ['aoen143@gmail.com', 'manishgupta3950@gmail.com']

# Email Connection to the server
email_conn = smtplib.SMTP(host, port)

email_conn.ehlo()  # can be ommited

# Creating a secured layer
email_conn.starttls()

# Now , login
email_conn.login(username, password)

# After successfully login, now sending email

email_conn.sendmail(from_email, to_list, "Hello ! This is a test messages")


email_conn.quit()

print("Another Method")
# also handle errors


from smtplib import SMTP
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

# Email Connection to the server
email_conn2 = SMTP(host, port)

email_conn2.ehlo()

# Creating a secured layer
email_conn2.starttls()

try:
    email_conn2.login(username, "abc")
    email_conn2.sendmail(from_email, to_list, "Fuck")

except SMTPAuthenticationError:
    print("Could Not login")
email_conn2.quit()














