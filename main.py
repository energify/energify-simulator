from Community import Community
from Person import Person
from profile import tipo
from House import House
import sys
import json
import time
import isodate
import os
from http_client import update
import dateutil.parser as dp
import csv
from http_client import update_price
from datetime import datetime

#argumento 1 -> local/nome do ficheiro
#argumento 2 -> tempo de simulacao do ficheiro para um ano em minutos
#argumento 3 -> nome
#argumento 4 -> numero  


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

def main(arg):

    make_json('locais/csv/' + arg[1] + '.csv', 'locais/json/' + arg[1] + '.json')



    with open('locais/json/' + arg[1]+str('.json'), 'r') as f:
        community_times = json.load(f)
    
    com = None

    if len(arg) == 5 and str(arg[3]+'.json') not in os.listdir('comunidades/'):
        com = Community(arg[1], int(arg[4]))

        


        community_data = {}
        i = 1
        print(com.houses)
        for house in com.houses:
            community_data[str(i)] = {}
            community_data[str(i)]['area'] = house.area
            community_data[str(i)]['sell'] = house.sell 
            community_data[str(i)]['buy'] = house.buy 
            j = 1
            community_data[str(i)]['people'] = {}
            for person in house.persons:
                community_data[str(i)]['people'][str(j)] = person.profile[0]
                j+=1
            
            i+=1

        with open('comunidades/' + arg[3] + str('.json'), 'w') as f:
            json.dump(community_data,f, indent=4)

    else:
        with open('comunidades/' + arg[3]+str('.json'), 'r') as f:
            load = json.load(f)

        house_list = []

        for house in load:
            area = load[house]['area']
            people_list = []
            for person in load[house]['people']:
                for lista in tipo:
                    if lista[0] == load[house]['people'][person]:
                        
                        people_list.append(Person(lista))
                        break
            h = House(area,people_list,arg[1])
            h.sell = load[house]['sell']
            h.buy = load[house]['buy']
            update_price(h.sell,h.buy,h.token)
            house_list.append(h)

        com = Community(arg[1],house_list)



            

    time_interval = str(isodate.parse_duration(community_times['0']['Period'])).split(':')
    time_interval = (int(time_interval[0])*60 + int(time_interval[1]))*60
    year = 31536000
    x = int(arg[2])*60
    time_2_send = (15*x)/year
    #print(time_2_send)

    time1 = 0

    house_dict = {}

    for a in com.houses:
        if a not in house_dict:
            house_dict[a] = []

    
    while True:
        time1 = time.time()
        timestamp = dp.parse(community_times['0']['PeriodStart']).timestamp()
        end_timestamp = timestamp
        for index in community_times:
            values = []
            for a in com.houses:
                house_dict[a] = []
                values.append(round(a.production(index) - a.consumption(index),3))

            end_timestamp += time_interval

            while(timestamp < end_timestamp):

                cont = 0
                for a in com.houses:
                    house_dict[a].append({'timestamp': timestamp, 'value': values[cont]})
                    cont+=1

                time.sleep(time_2_send)
                timestamp += 15

            for a in com.houses:
                #print(len(house_dict[a]))
                print(update(house_dict[a],a.token).json(), datetime.fromtimestamp(timestamp))
        print(time.time() - time1)
        
        break

main(sys.argv)