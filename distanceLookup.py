from graphClass import *


def lookUp(list,dict,v1,v2):
    print("Distance between:")
    print(dict[v1]['Name'])
    print("and")
    print(dict[v2]['Name'])

    if v1 > v2:
        v1, v2 = v2, v1

    print(list[v2][v1])
