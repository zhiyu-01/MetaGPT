import requests

url = 'http://127.0.0.1:8080/v1'

response = requests.post(url=url)

if response.status_code == 200:
    print(response.json())
else:
    print('failed')
