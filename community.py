import csv

import isodate

from profile import *
import numpy as np
import math
import json
from datetime import datetime
import dateutil.parser


def generate_random(num, min, max, mid):
    arr1 = np.random.randint(min, mid, math.ceil(num / 2))
    arr2 = np.random.randint(mid, max, math.ceil(num / 2))
    if num % 2 == 1:
        arr2 = arr2[0:-1]
    return np.concatenate((arr1, arr2)).tolist()


def make_json(csvFilePath, jsonFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        key = 0
        for rows in csvReader:
            data[key] = rows
            key+=1

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

class Community:
    def __init__(self, local, num_houses):
        make_json(local + '.csv', local + '.json')
        rand_area = generate_random(num_houses, 5, 50, 15)
        rand_people = generate_random(num_houses, 1, 6, 3)
        self.houses = [House(rand_area.pop(), rand_people.pop(),local) for i in range(num_houses)]


class House:
    def __init__(self, area, num_persons,local):
        self.area = area
        self.local = local
        self.persons = [Person(daily5) for i in range(num_persons)]

    def production(self):
        with open(self.local+str('.json'), 'r') as f:
            data = json.load(f)

        #today = dateutil.parser.parse(datetime.datetime.now().replace(microsend=0).isoformat()+str('Z'))
        today = dateutil.parser.parse('2020-12-22T15:00:00Z')
        time_interval = isodate.parse_duration(data['0']['Period'])


        irradiance = 0
        for interval in data:
            if (today - dateutil.parser.parse(data[interval]['PeriodStart'])) <= time_interval:
                irradiance = int(data[interval]['Dni'])
                break


        return (self.area * 0.20 * irradiance * 1)/1000

    def consumption(self):
        return 0


class Person:
    def __init__(self, profile):
        self.profile = profile
