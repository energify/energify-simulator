from Community import Community
import sys
import json
import time
import isodate

#argumento 1 -> local/nome do ficheiro
#argumento 2 -> tempo de simulacao do ficheiro para um ano em minutos

def main(arg):
    com = Community('test', int(arg[1]))

    with open(com.local+str('.json'), 'r') as f:
        community_times = json.load(f)

    time_interval = str(isodate.parse_duration(community_times['0']['Period'])).split(':')
    time_interval = int(time_interval[0])*60 + int(time_interval[1])
    year = 525600
    x = int(arg[2])
    time_2_send = time_interval*x/year

    time1 = 0

    while True:
        time1 = time.time()
        for index in community_times:
            time_now = community_times[index]['PeriodStart']
            #print(time_now)
            for a in com.houses:
                oi = round(a.production(time_now) - a.consumption(time_now),3)

            print(index)
            #time.sleep(time_2_send)
        print(time1 - time.time())

main(sys.argv)