import requests	    #BeautifulSoup和requets的库都是要另外安装的，网上有教程		
import re
import time
from bs4 import BeautifulSoup

# imgURL = "http://203.34.153.97:10000/upload/1.png"
# imgresponse=requests.head(imgURL).headers	
# print(type(imgresponse))
# print(imgresponse['content-length'])


imgURL = "http://203.34.153.97:10000/upload/1.png"
imgresponse=requests.get(imgURL,stream = True)
image = imgresponse.content	
print(type(image))
print(len(image))
# print(image)

