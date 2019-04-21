import requests

data={
	'name':'cxw',
	'age':20,
	'date':'2.29'
}
headers={ 
	'User-Agent':"Google Chrome/68.0.3440.106 Mac OS X"
}

# response = requests.get("http://httpbin.org/get?name=cxw&age=20&date=2.29")
response = requests.get("http://httpbin.org/get",params=data,headers=headers)  #与上一行相同




print(response)
print(response.status_code)
print(response.text)
print(response.cookies)
