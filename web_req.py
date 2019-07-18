import requests

url =  ''
data = dict{}

data['search'] = 'jea'


resp = requests.get(url, params=None)
resp = requests.post(url, data=data)