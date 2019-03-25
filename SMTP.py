import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import time 

gmail_user = 'cxw63377312@gmail.com'
gmail_password = 'cxw63377312cxw' # your gmail password

attachment_name="code.jpg"
# msg = MIMEText('hello cxws')
# msg['Subject'] = 'sass深爱的1'
# msg['From'] = gmail_user
# msg['To'] = '826697909@qq.com'

def sendImg():
	result = 0
	msg = MIMEMultipart()
	msg['Subject'] = '1OK'
	msg['From'] = gmail_user
	msg['To'] = '826697909@qq.com'
	content = MIMEText("email_content", _charset='gbk')   # add email content  ,coding is gbk, becasue chinese exist
	msg.attach(content)

	# attachment_name="code.jpg"
	# attachment_file="/Users/ccc/Desktop/my\ python\ code/"
	with open(attachment_name, 'rb') as attachment:
		attachment = MIMEImage(attachment.read(),  _subtype='octet-stream')
		attachment.add_header('Content-Disposition', 'attachment', filename = ('gbk', '', attachment_name))
	    # make sure "attachment_name is chinese" right
		msg.attach(attachment)

	try:
		print("contenting to the server")
		server = smtplib.SMTP_SSL('smtp.163.com',465,timeout=5)
		server.ehlo()
		print("contented to the server")
	except:
		print('CONNECT ERROR ****')
	else:
		try:
			print("logining to the server")
			server.login(gmail_user, gmail_password)
			print("logined to the server")
		except:
			print('LOGIN ERROR ****')
		else:
			server.send_message(msg)
			server.quit()
			print('Email sent!')
			result=1
	return result



