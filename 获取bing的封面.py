import requests	    #BeautifulSoup和requets的库都是要另外安装的，网上有教程		
import re
import time
from bs4 import BeautifulSoup
r=requests.get('https://cn.bing.com')    #这里是bing的网址，通过requests库的get请求来获取bing网页的源代码
html=r.text				#这一步是把获取来的格式变成str
matchObj = re.findall('src\S+jpg',html)	#这里是一个正则表达式，用来获取图片的url地址
matchObj = "".join(matchObj)	#这一步把findall所返回的list类型变为str
# for i in matchObj:
defaultURL="https://cn.bing.com/"
changedURL=matchObj[6:]		#截取，从第五位开始
imgURL = defaultURL+changedURL
print(defaultURL)
# print(imgURL)				#这里就是一个能够使用的url地址了

#我们可以先看一下爬取来的地址

#接下来的任务就是把图片下载到本地
#我们先以流的方式打开
imgresponse = requests.get(imgURL, stream=True)   #以流的方式打开
image = imgresponse.content  #用。content获取其中的内容
# localtime = time.asctime( time.localtime(time.time()) )
#应为我接下去要用现在的时间来命名这张图片，所以我先获得一下当前的时间
localtime = time.strftime("%Y-%m-%d", time.localtime()) 
address="./bing/"  #保存地址。    　./就表示保存在当前的工作目录
imgName=address+localtime+".jpg" 	#加上时间和.jpg作为名字


#接下来就是将文件写入

#利用open这个方法来打开一个文件。 文件的名称就是我们上面取好的imgName
try:
    with open(imgName,"wb") as jpg: 
        jpg.write(image) #用.write写入
except IOError:
    print("IO Error\n")
finally:
    jpg.close 	#最后关闭就行了。   

#好。 我们接下来就来运行一下


# 可以看到运行成功			我们取文件夹里看看文件是否存在

