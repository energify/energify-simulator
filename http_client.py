import requests
import json

url = 'http://localhost:3000/'
#url = 'http://13.84.134.143:3000/'
headers = {'content-type':'application/json', 'accept':'application/json'}

def login(email,password):
    data = {'email': email,'password':password}
    response = requests.post(url+'auth/login', data=json.dumps(data), headers=headers)
    return response.json()['accessToken']

def register(name,email,password,id):
    data = {'name':name, 'email': email,'password': password, 'hederaAccountId': id}
    response = requests.post(url+'auth/register', data=json.dumps(data), headers=headers)
    return response
    
def update_price(sell, buy, auth_token):
    data = {'sellPrice' : sell, 'buyPrice' : buy}
    headers['authorization'] = auth_token
    response = requests.put(url+'users/prices', data=json.dumps(data), headers=headers)
    headers.pop('authorization')
    return response

def update(measurement,auth_token):
    data = {'measures':measurement}
    headers['authorization'] = auth_token
    response = requests.put(url+'meters/user', data=json.dumps(data), headers=headers)
    headers.pop('authorization')
    return response

    
    
