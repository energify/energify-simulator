from Person import *
from profile import daily5
import json
import dateutil.parser
import isodate
import random
import datetime

class House:
    def __init__(self, area, num_persons,local):
        self.area = area
        self.local = local
        self.persons = [Person(daily5) for i in range(num_persons)]

    def production(self, time_now):
        with open(self.local+str('.json'), 'r') as f:
            data = json.load(f)

        #today = dateutil.parser.parse(time_now.replace(microsend=0).isoformat()+str('Z'))
        today = dateutil.parser.parse(time_now)
        time_interval = isodate.parse_duration(data['0']['Period'])


        irradiance = 0
        for interval in data:
            interval_details = data[interval]
            if (today - dateutil.parser.parse(interval_details['PeriodStart'])) <= time_interval:
                irradiance = int(interval_details['Dni'])
                break
                    

        return round((self.area * (random.randint(15,22)/100) * irradiance * 1)/1000, 3)

    def consumption(self,time_now):
        people_percent = [1, 0.75, 0.5, 0.3, 0.2, 0.1]
        today = dateutil.parser.parse(time_now)
        hours  = today.hour
        cons = 0
        for p in range(len(self.persons)):
            cons += self.persons[p].profile[hours] * people_percent[p]
        return cons