import requests

url =  ''
data = dict{}

data['search'] = 'jea'


resp1 = requests.get(url, params=None)
resp2 = requests.post(url, data=data)