import requests
import json

url = 'http://energify.av.it.pt/'
#url = 'https://e679f44f3fa0.ngrok.io/'
headers = {'content-type':'application/json', 'accept':'application/json'}

def login(email,password):
    data = {'email': email,'password':password}
    response = requests.post(url+'users/login', data=json.dumps(data), headers=headers)
    return response.json()['accessToken']

def register(name,email,password,born_at,cc):
    data = {'name':name, 'email': email,'password': password, 'birthday': born_at, 'cc': cc}
    response = requests.post(url+'users/register', data=json.dumps(data), headers=headers)
    return response

def complete(nif,address,hedera_id,auth_token):
    data = {'nif':nif, 'address': address,'hederaAccountId': hedera_id}
    headers['authorization'] = auth_token
    response = requests.put(url+'users/complete', data=json.dumps(data), headers=headers)
    headers.pop('authorization')
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

    
    
