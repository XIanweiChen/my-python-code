from selenium import webdriver 
import time
from bs4 import BeautifulSoup

try:
	browser = webdriver.Chrome("../chromedriver")
	browser.get('http://www.qqenglish.com/bn/32071.htm')
	content = browser.find_elements_by_tag_name('p')
	for i in content:
		print(i.text)
		print()
	
except Exception as e:
	raise
else:
	pass
finally:
	browser.close()
