import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from']= 'Mr.abc'
email['to']= 'Sender@gmail.com'
email['subject']='you won something :)'

email.set_content(html.substitute({'name':'Abc'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('abc@gmail.com','Your_password')
	smtp.send_message(email)
	print('all good boss! email has send to neha')

	