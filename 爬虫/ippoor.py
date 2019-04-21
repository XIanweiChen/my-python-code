import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
result = requests.get('http://www.xicidaili.com/nn/1',headers=headers)
print(result)
print(result.text)