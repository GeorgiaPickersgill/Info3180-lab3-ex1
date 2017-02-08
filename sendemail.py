import smtplib
from_addr = 'username@gmail.com'
to_addr  = 'username@gmail.com'
from_name = 'Georgia Pickersgill'
to_name = 'the genius'
subject = 'baby you the best'
msg = 'Put in that work and go get that dinero'
message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""
message_to_send = message.format(from_name, from_addr, to_name,
                to_addr, subject, msg)
# Credentials (if needed)
username = 'g.j.pickersgill@gmail.com'
password = 'jevlahmzmsljxofq'
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()