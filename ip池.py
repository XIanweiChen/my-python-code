# encoding:utf-8
import requests  # 导入requests模块用于访问测试自己的ip
import random
from requests.exceptions import ReadTimeout,RequestException
pro = ['118.190.95.35:9001','118.190.95.43:9001']  # 在(http://www.xicidaili.com/wt/)上面收集的ip用于测试
# 没有使用字典的原因是 因为字典中的键是唯一的 http 和https 只能存在一个 所以不建议使用字典

#  你的请求头信息
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
# url = 'http://www.xicidaili.com/nn/1'  # 你用于测试自己ip的网站
url = 'http://www.lol.com'
try:
	request = requests.get(url, proxies={'http':random.choice(pro)}, headers=head,timeout=5)  # 让问这个网页  随机生成一个ip
	request.encoding = request.apparent_encoding  # 设置编码 encoding 返回的是请求头编码  apparent_encoding 是从内容网页中分析出的响应内容编码方式
	print(request)
	print(request.text)  # 输出返回的内容
except ReadTimeout:
	print("ReadTimeout")
except RequestException:
	print("RequestException")