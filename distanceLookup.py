from graphClass import *


def lookUp(list,dict,v1,v2):
    print("Distance between:")
    print(dict[v1]['Name'])
    print("and")
    print(dict[v2]['Name'])

    if v1 > v2:
        v1, v2 = v2, v1

    print(list[v2][v1])

def minDist(graph, address_dict, start_point):
    print("Starting Index: ", start_point)
    print("Starting Address: ", address_dict.get(start_point))
    print(" ")
    print("Next Closest Point:")

    min_distance = 1000
    finish_min = start_point

    for i in graph.edge_weights:
        # is the start point in the key
        start, finish = i

        distance = graph.edge_weights.get(i)
        if start == start_point:
            # print("Start: ", start, " Finish: ", finish, " Distance between: ", distance)

            if distance > 0 and distance < min_distance:
                min_distance = distance
                finish_min = finish
    print(min_distance, " to ", finish_min)

        #print(i)
        #if start_point


        # Store the distance
        # Check if the distance is between current min and zero
        # Swap into min