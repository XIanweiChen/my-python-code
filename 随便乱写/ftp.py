from ftplib import FTP
import os.path

#设置FTP连接信息
# 149.28.93.112
# 203.34.153.97
address= '203.34.153.97'
port= 20000
#FTP用户名
user_name= '123'
#FTP密码
password= '123'

#本地要上传的文件名
local_file_name="/Users/ccc/Desktop/2.png"
#FTP中要下载的文件名
remote_file_name="2.png"



def upload_file(local_file_name):
    try:
        ftp = FTP()
        ftp.set_debuglevel(1)
        ftp.connect(address,port)
        ftp.login(user_name,password)
        #文件上传到FTP服务器的路径（前提是路径要存在，否则会报错）
        remote_path="/"#如：将本地文件上传到FTP根目录
        ftp.cwd(remote_path)#切换到此路径
        file=open(local_file_name,'rb')
        #如果参数 pasv 为真，打开被动模式传输 (PASV MODE) ，否则，如果参数 pasv 为假则关闭被动传输模式。
        # ftp.set_pasv(1)    
        ftp.storbinary('STOR %s' % os.path.basename(local_file_name),file)    
        file.close()    
        ftp.close()
        print("文件上传完成")
    except Exception as e:
        print("文件上传失败...")
        print(str(e))

def download_file(remote_file_name):
    try:
        #创建ftp对象实例 
        ftp = FTP()  

        ftp.set_debuglevel(1)

        #连接接FTP
        ftp.connect(address, port)
        #通过账号和密码登录FTP服务器 
        ftp.login(user_name,password)
        #如果参数 pasv 为真，打开被动模式传输 (PASV MODE) ，否则，如果参数 pasv 为假则关闭被动传输模式。
        ftp.set_pasv(1)
        #设置FTP上文件下载到本地的位置
        local_path="./"#如：将文件下载到当前程序所在目录中的local子目录中，也可以使用绝对路径
        #为准备下载到本地的文件，创建文件对象（默认为远程下载的文件名，也可自定义）
        local_file_name=local_path + os.path.basename(remote_file_name)
        file = open(local_file_name, 'wb')
        #从FTP服务器下载文件到前一步创建的文件对象，其中写对象为file.write，1024是缓冲区大小  
        ftp.retrbinary('RETR '+remote_file_name,file.write,1024)  
        #关闭下载到本地的文件  
        #提醒：虽然Python可以自动关闭文件，但实践证明，如果想下载完后立即读该文件，最好关闭后重新打开一次 
        file.close() 
        #关闭FTP客户端连接
        ftp.close()
        print("文件下载完成")
    except Exception as e:
        print("文件下载失败...")
        print(str(e))


# upload_file(local_file_name)
download_file(remote_file_name)