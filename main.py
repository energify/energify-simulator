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

#argumento 1 -> local/nome do ficheiro
#argumento 2 -> tempo de simulacao do ficheiro para um ano em minutos
#argumento 3 -> nome
#argumento 4 -> numero  

def main(arg):


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
            j = 1
            community_data[str(i)]['people'] = {}
            for person in house.persons:
                community_data[str(i)]['people'][str(j)] = person.profile[0][0]
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

            house_list.append(House(area,people_list,arg[1]))

        com = Community(arg[1],house_list)




            

    time_interval = str(isodate.parse_duration(community_times['0']['Period'])).split(':')
    time_interval = int(time_interval[0])*60 + int(time_interval[1])
    year = 525600
    x = int(arg[2])
    time_2_send = ((time_interval*x)/year)*60
    #print(time_2_send)


    while True:
        for index in community_times:
            for a in com.houses:
                update(round(a.production(index) - a.consumption(index),3),a.token)

            #print(index)
            time.sleep(time_2_send)
        break

main(sys.argv)