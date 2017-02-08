import smtplib
from_addr = 'username@gmail.com'
from_name = 'Brittney S'
to_name = 'David'
to_addr  = 'david@someemail.com'
subject = 'Test Mail'
message = """From: {} <{}>
To: {} <{}> 
Subject: {}
{}
"""
message_to_send = message.format(from_name, from_addr, to_name,
                to_addr, subject, message)
# Credentials (if needed)
username = 'username@gmail.com'
password = 'password'
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()
