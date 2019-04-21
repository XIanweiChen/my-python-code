import os
import time
import datetime
import sys,time
 
print("正在下载......")
for i  in  range(11):
    sys.stdout.write("->"+"%"+str(i))
    sys.stdout.flush()
    time.sleep(0.2)
print("\n"+"下载完成")


	

# print(os.path.getsize(r'"/Users/ccc/Desktop/my\ python\ code/进度条.py"')


# import requests	
# import os
# import time
# imgURL = "http://203.34.153.97:10000/upload/1.png"
# imgresponse = requests.get(imgURL, stream=True)   #以流的方式打开
# image = imgresponse.content  #用。content获取其中的内容
# # localtime = time.asctime( time.localtime(time.time()) )
# #应为我接下去要用现在的时间来命名这张图片，所以我先获得一下当前的时间
# localtime = time.strftime("%Y-%m-%d", time.localtime()) 
# address="./"  #保存地址。    　./就表示保存在当前的工作目录
# imgName=address+localtime+".png" 	#加上时间和.jpg作为名字


# #接下来就是将文件写入

# #利用open这个方法来打开一个文件。 文件的名称就是我们上面取好的imgName
# try:
# 	jpg=open(imgName,"wb") 
# 	# for i in image:	
# 	# 	jpg.write(bytes(i))
# 	# 	print(i)
# 	jpg.write(image)
# 	jpg.close()
#     # jpg.write(image)
# except IOError:
#     print("IO Error\n")
# finally:
#     jpg.close 	#最后关闭就行了。 