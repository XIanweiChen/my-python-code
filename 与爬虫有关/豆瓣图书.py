import requests  
import random
import re
from requests.exceptions import ReadTimeout,RequestException

pro = ['219.141.153.41:80','118.190.95.35:9001','118.190.95.43:9001'] 

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
url = 'https://book.douban.com'  # 你用于测试自己ip的网站
try:
	request = requests.get(url, proxies={'http':random.choice(pro)}, headers=head,timeout=5)  # 让问这个网页  随机生成一个ip
	request.encoding = request.apparent_encoding  # 设置编码 encoding 返回的是请求头编码  apparent_encoding 是从内容网页中分析出的响应内容编码方式
	html = request.text  # 输出返回的内容
	print(request)
	# pattern = re.compile('.*?href="(.*?)"\s+title="(.*?)".*?more-meta.*?author">(.*?).*?year">(.*?).*?',re.S)
	result = re.findall('<div class="cover">.*?<a href=".*?".*?<h4 class="title">(.*?)</h4>',html,re.S)
	# result = re.findall(pattern,html)
	print(result)

except ReadTimeout:
	print("ReadTimeout")
except RequestException:
	print("RequestException")