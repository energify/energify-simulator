from Community import Community
import sys


def main(arg):
    com = Community('test', int(arg[1]))

    areas = []
    people = []

    for a in com.houses:
        areas.append(a.area)
        people.append(len(a.persons))

    print(areas)
    print(people)
    return None

main(sys.argv)