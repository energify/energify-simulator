from Person import *
from profile import tipo
import json
import dateutil.parser
import isodate
import random
import datetime

class House:
    def __init__(self, area, persons,local):

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
        return round((self.area * (random.randint(15,22)/100) * irradiance * 1)/1000, 3)

    def consumption(self,index):
        people_percent = [1, 0.75, 0.5, 0.3, 0.2, 0.1]
        time_now = self.data[index]['PeriodStart']
        today = dateutil.parser.parse(time_now)
        hours  = today.hour
        cons = 0
        for p in range(len(self.persons)):
            cons += self.persons[p].profile[1][0][hours] * people_percent[p]
        return cons