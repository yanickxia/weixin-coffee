__author__ = 'yann'


# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
from weixin import const

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

msg = MIMEText("test")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % 'xxx'
msg['From'] = const.EMAIL_FROM
msg['To'] = 'me.yan.xia@qq.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP(const.EMAIL_STMP)
s.send_message(msg)
s.quit()
