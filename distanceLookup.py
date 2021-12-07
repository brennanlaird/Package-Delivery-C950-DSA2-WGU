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


def next_nearest(truck, graph):
    # Sets up the minimum as an arbritrary high value and sets the current location to the location of the truck.
    min = 1000
    current_loc = truck.currentLocation

    # For loop finds the minimum next distance among all the packages loaded on the truck.
    for package in truck.truck_content:
        # Pull the next address index from the current package.
        next_location = package[10]
        # x represents a tuple of the current and next location that is then pulled from the graph edge weights.
        x = current_loc, next_location
        next_distance = graph.edge_weights.get(x)

        # If the next distance is less than the minimum, set that to be the next location to deliver to.
        if next_distance < min:
            min = next_distance
            next_stop = next_location
            # Gets the index location of the current package in the truck.
            index = truck.truck_content.index(package)
    # Returns the trucks next stop and the index location of the package
    return next_stop, index
