from bs4 import BeautifulSoup 
import requests
import re
import time
local = time.strftime("%Y.%m.%d")
print (local)
url = 'https://cn.bing.com/'
con = requests.get(url)
content = con.text
reg = r"(https://cn.bing.com/)"
a = re.findall(reg, content)
print(a)

	









# url_session = requests.Session()
# req = url_session.get(url).text
# soup = BeautifulSoup(req, 'html.parser')
# phone_html = soup.find_all(name = 'span', attrs = {'class':"p-price"})
