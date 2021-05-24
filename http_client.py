import requests
import json

url = 'http://energify.av.it.pt/'
#url = 'https://48fe88deadd3.ngrok.io/'
headers = {'content-type':'application/json', 'accept':'application/json'}

def login(email,password):
    data = {'email': email,'password':password}
    response = requests.post(url+'auth/login', data=json.dumps(data), headers=headers)
    print(json.dumps(response.json(),indent=4))
    return response.json()['accessToken']

def register(name,email,password):
    data = {'name':name, 'email': email,'password': password}
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

    
    
