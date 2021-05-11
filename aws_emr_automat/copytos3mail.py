import smtplib

sender = 'sender@123mail.com'
PASSWORD = 'mail_password'
receivers = ['receiver1@abcmail.com', 'receiver2@wxymail.com']

message = """From: sender <sender@123mail.com>
To: receiver 1 <receiver1@abcmail.com>, receiver 2 <receiver2@wxymail.com>
Subject: JOB - Copy data to S3 status

Successfully copied data.
"""

try:
   smtpObj = smtplib.SMTP(host='SMTP_HOST_ADDR', port=port_no)
   smtpObj.starttls()
   smtpObj.login(sender, PASSWORD)
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")
   
smtpObj.quit()