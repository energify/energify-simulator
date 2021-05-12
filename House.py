from Person import *
from profile import tipo
import json
import dateutil.parser
import isodate
import random
import datetime
import string
from http_client import *

def gen_rand_string(length):
    letters = string.ascii_lowercase
    res = ''.join(random.choice(letters) for i in range(length))
    return res



class House:
    def __init__(self, area, persons,local):
        self.password = gen_rand_string(10)
        self.email = None
        while True:
            self.email = gen_rand_string(20)+'@energify.pt'
            response = register(self.password,self.email,self.password,'2000-02-23',str(random.randint(100000000,999999999))) 
            print(response.json())
            if 'statusCode' not in response.json():
                break

        self.token = login(self.email,self.password)

        while True:
            response = complete(str(random.randint(100000000,999999999)),gen_rand_string(50),gen_rand_string(20),self.token)
            print(response)
            if 'statusCode' not in response.json():
                break

        self.token = login(self.email,self.password)
        
        update_price(4,5,self.token)

        self.local = local
        self.area = area
        with open('locais/json/' + local+str('.json'), 'r') as f:
            self.data = json.load(f)

        self.time_interval = isodate.parse_duration(self.data['0']['Period'])

        if isinstance(persons,int):
            self.persons = [Person(tipo[0]) for i in range(persons)]
        else:
            self.persons = persons

    def production(self,index):
        irradiance = int(self.data[index]['Dni'])   
        res = round((self.area * (random.randint(15,22)/100) * irradiance * 1)/1000, 3)
        return res

    def consumption(self,index):
        people_percent = [1, 0.75, 0.5, 0.3, 0.2, 0.1]
        time_now = self.data[index]['PeriodStart']
        today = dateutil.parser.parse(time_now)
        hours  = today.hour
        temp = float(self.data[index]['AirTemp'])
        prof_temp = None
        if temp <= 5:prof_temp = 0
        elif temp <= 10: prof_temp = 1
        elif temp <= 15: prof_temp = 2
        elif temp >= 35: prof_temp = 5
        elif temp >= 30: prof_temp = 4
        elif temp >= 25: prof_temp = 3
        else: prof_temp = 6

        cons = 0
        for p in range(len(self.persons)):
            cons += self.persons[p].profile[1][0][hours] * people_percent[p]
        return cons