from Person import *
from profile import tipo
import json
import dateutil.parser
import isodate
import random
import datetime
import string
from http_client import *
import numpy as np

def gen_rand_string(length):
    letters = string.ascii_lowercase
    res = ''.join(random.choice(letters) for i in range(length))
    return res

def gen_value():
    lista = np.random.normal(1.1,0.01,20)
    index = random.randint(0,19)
    while(lista[index] > 1.20 or lista[index] < 1.00):
        index = random.randint(0,19)
    return lista[index]





class House:
    def __init__(self, area, persons,local):
        '''self.password = gen_rand_string(10)
        self.email = None
        while True:
            self.email = gen_rand_string(20)+'@energify.pt'
            response = register(self.password,self.email,self.password) 
            print(response.json())
            if 'statusCode' not in response.json():
                break'''

        self.email = 'rob@energify.pt'
        self.password = '1234'
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiUm9iIiwiaWQiOiI2MGFiYjIwYmE4MDgxMjJjMzdhYTJiN2IiLCJlbWFpbCI6InJvYkBlbmVyZ2lmeS5wdCIsImlhdCI6MTYyMTg2NjYzMX0.rvw1hleW1GrN3P9neL4cq-dSBavJx79S6gC2XR2Thf0'
        #self.token = login(self.email,self.password)
        #print(self.token)
       
        self.sell = round(gen_value(),2)
        self.buy = round(self.sell+0.02,2)


        #print(sell,buy)

        
        update_price(self.sell,self.buy,self.token)

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
        info = self.data[index]
        time_now = info['PeriodStart']
        today = dateutil.parser.parse(time_now)
        hours  = today.hour
        temp = float(info['AirTemp'])
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