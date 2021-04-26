from community import *
import sys


def main(arg):
    com = Community('test', int(arg[1]))

    for a in com.houses:
        print(a.production(), a.area, len(a.persons))
    return None

main(sys.argv)