import requests

url =  'http://127.0.0.1:5000'
data = dict()

data['search'] = "jea"


resp1 = requests.get(url, params=None)
resp2 = requests.post(url, data=data)
