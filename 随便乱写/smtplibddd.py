import smtplib
import sys
import email.mime.text
# my test mail
mail_username='cxw63377312@gmail.com'
mail_password='201619630302Cc'
from_addr = mail_username
to_addrs=('826697909@qq.com')
 
# HOST & PORT
HOST = 'smtp.gmail.com'
PORT = 25
 
# Create SMTP Object
smtp = smtplib.SMTP()
print ('connecting ...')
 
# show the debug log
smtp.set_debuglevel(1)
 
# connet
try:
    print (smtp.connect(HOST,PORT))
except:
    print ('CONNECT ERROR ****')
# gmail uses ssl
smtp.starttls()
# login with username & password
try:
    print ('loginning ...')
    smtp.login(mail_username,mail_password)
except:
    print ('LOGIN ERROR ****')

# fill content with MIMEText's object 
msg = email.mime.text.MIMEText('Hi ,I am cxw')
msg['From'] = from_addr
msg['To'] = ';'.join(to_addrs)
msg['Subject']='ojbkss'




print (msg.as_string())
smtp.sendmail(from_addr,to_addrs,msg.as_string())
smtp.quit()
