import requests
import re
import time
from bs4 import BeautifulSoup
r = requests.get('https://cn.bing.com/')
html = r.text
matchObj = re.findall('src\S+jpg',html)

print(matchObj)