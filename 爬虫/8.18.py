#coding:utf-8
import requests
import time 
# imgUrl = "https://cn.bing.com/az/hprichbg/rb/CanolaBeehives_ZH-CN9545312261_1920x1080.jpg"   #请求图片的url
imgUrl = "https://cn.bing.com/az/hprichbg/rb/Unisphere_ZH-CN7027287379_1920x1080.jpg"
imgresponse = requests.get(imgUrl, stream=True)   #以流的方式打开
image = imgresponse.content
localtime = time.asctime( time.localtime(time.time()) )
address="./"  #保存地址
try:
    with open(address+localtime+"code.jpg" ,"wb") as jpg: 
        jpg.write(image)
except IOError:
    print("IO Error\n")
finally:
    jpg.close




