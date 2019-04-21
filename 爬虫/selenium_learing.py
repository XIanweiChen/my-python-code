from selenium import webdriver 
import time
from bs4 import BeautifulSoup

try:
	browser = webdriver.Chrome("./chromedriver")
	browser.get('https://wenku.baidu.com/view/2c48bbd1dc3383c4bb4cf7ec4afe04a1b071b0fb.html?rec_flag=default')
	# input = browser.find_element_by_id('kw')

	# bt = browser.find_element_by_class_name('down-arrow')
	# bt.click()
	time.sleep(5)
	content = browser.find_elements_by_class_name('reader-word-layer')
	# input.send_keys('中文')
	# input.send_keys(Keys.ENTER)

	# html = browser.page_source
	for i in content:
		if i.text==" ":
			print("")
		print(i.text,end="")
	
except Exception as e:
	raise
else:
	pass
finally:
	browser.close()


# bf = BeautifulSoup(html)
# texts = bf.find_all('p', class_ = 'reader-word-layer')
# print(texts)