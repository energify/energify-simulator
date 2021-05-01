import csv
import numpy as np
import math
import json
from House import *
import collections



def generate_random(num, min, max, mid):
    lst = []
    while len(lst) < math.ceil(num/2):
        rand = np.random.exponential((min+mid)/2,100)
        rand = (rand - mid) * -1
        for elem in rand:
            elem = math.floor(elem)
            if elem >= min and elem <= mid:
                lst.append(elem)
                if len(lst) == math.ceil(num/2):
                    break

    while len(lst) < num:
        rand = np.random.exponential((mid+max)/2,100)
        for elem in rand:
            elem = math.floor(elem)
            if elem >= mid and elem <= max:
                lst.append(elem)
                if len(lst) == num:
                    break

    return lst




def make_json(csvFilePath, jsonFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
        cont = 0
        for rows in csvReader:
            data[str(cont)] = rows
            cont+=1

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        json.dump(data,jsonf, indent=4)

class Community:
    def __init__(self, local, num_houses):
        make_json(local + '.csv', local + '.json')
        rand_area = generate_random(num_houses, 5, 50, 15)
        rand_people = generate_random(num_houses, 1, 6, 3)
        self.houses = [House(rand_area.pop(), rand_people.pop(),local) for i in range(num_houses)]






