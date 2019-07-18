import requests

index_url = 'http://localhost:5000/'
index_data = dict()
index_data['search'] = 'jea'

login_url = 'http://localhost:5000/login'
login_data = {'username': 'testuser', 'password': 'testpassword'}

resp1 = requests.get(index_url, params=None)
resp2 = requests.post(index_url, data=index_data)
resp3 = requests.get(login_url, params=None)
resp4 = requests.post(login_url, data=login_data)

