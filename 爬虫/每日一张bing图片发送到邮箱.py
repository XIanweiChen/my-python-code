import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import requests
import re
import time
from bs4 import BeautifulSoup

r=requests.get('https://cn.bing.com')
html=r.text
<<<<<<< HEAD
matchObj = re.findall('url:\S+?jpg',html)	#这里是一个正则表达式，用来获取图片的url地址
matchObj = "".join(matchObj[0])	#这一步把findall所返回的list类型变为str
=======
matchObj = re.findall('src\S+jpg',html)
matchObj = "".join(matchObj)
>>>>>>> 26342a1708dfc2ce4db78851bc924815f8d01555
# for i in matchObj:
defaultURL="https://cn.bing.com/"
changedURL=matchObj[5:]
imgURL = defaultURL+changedURL
print(imgURL)

imgresponse = requests.get(imgURL, stream=True)   #以流的方式打开
image = imgresponse.content
# localtime = time.asctime( time.localtime(time.time()) )
localtime = time.strftime("%Y-%m-%d", time.localtime()) 
address="./bing/"  #保存地址
imgName=address+localtime+".jpg"
try:
    with open(imgName,"wb") as jpg: 
        jpg.write(image)
except IOError:
    print("IO Error\n")
finally:
    jpg.close






gmail_user = 'cintmain@163.com'
gmail_password = '201619630302Cc'# your gmail password
mail_tilte=time.asctime( time.localtime(time.time()) )
# attachment_name="code.jpg"
# msg = MIMEText('hello cxws')
# msg['Subject'] = 'sass深爱的1'
# msg['From'] = gmail_user
# msg['To'] = '826697909@qq.com'


def sendImg():
	result = 0
	msg = MIMEMultipart()
	msg['Subject'] = mail_tilte
	msg['From'] = gmail_user
<<<<<<< HEAD
	# msg['To'] = '415574154@qq.com'
=======
>>>>>>> 26342a1708dfc2ce4db78851bc924815f8d01555
	msg['To'] = '826697909@qq.com'
	content = MIMEText("This is today's Bing wallpaper.", _charset='gbk')   # add email content  ,coding is gbk, becasue chinese exist
	msg.attach(content)

	# attachment_name="code.jpg"
	# attachment_file="/Users/ccc/Desktop/my\ python\ code/"
	with open(imgName, 'rb') as attachment:
		attachment = MIMEImage(attachment.read(),  _subtype='octet-stream')
		attachment.add_header('Content-Disposition', 'attachment', filename = ('gbk', '', imgName))
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
while(sendImg()==0):
	time.sleep(3)
