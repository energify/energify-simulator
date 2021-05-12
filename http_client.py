import requests

url = 'https://energify.av.it.pt/'
headers = {'content-type':'application/json', 'accept':'application/json'}

def login(email,password):
    data = {'email': email,'password':password}
    response = requests.post(url+'users/login', data=data, header=headers)
    return response['accessToken']

def register(name,email,password,born_at,cc):
    data = {'name':name, 'email': email,'password': password, 'bornAt': born_at, 'cc': cc}
    response = requests.post(url+'users/register', data=data, header=headers)
    return response.status_code

def complete(nif,address,hedera_id,auth_token):
    data = {'nif':nif, 'address': address,'hederaAccountId': hedera_id}
    headers['authorization'] = auth_token
    response = requests.post(url+'users/complete', data=data, header=headers)
    headers.pop('authorization')

def update(measurement,auth_token):
    data = {'measurement':measurement}
    headers['authorization'] = auth_token
    response = requests.post(url+'users/complete', data=data, header=headers)
    headers.pop('authorization')

    
    
