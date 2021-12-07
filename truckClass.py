from distanceLookup import next_nearest
from packHash import *
from packClass import *


class Truck:
    # Define the truck object constructor.
    def __init__(self, truck_id, currentLocation, speed, capacity, truck_content, distance_traveled):
        self.truck_id = truck_id
        self.currentLocation = currentLocation
        self.speed = speed
        self.capacity = capacity
        self.truck_content = []
        self.distance_traveled = distance_traveled


# Any functions go here
def load_truck(truck, pack_table):
    pc = 0
    truck_packages = []
    while pc < truck.capacity:
        #truck_packages.append(pack_table.searchPackages(pc+1))
        truck.truck_content.append(PackageHashTable.searchPackage(pack_table, pc+1))
        #print(PackageHashTable.searchPackage(pack_table,pc+1))
        pc += 1

def deliver_packages(truck, graph):
    print("Drive around")
    pc = len(truck.truck_content)
    while pc > 0:
        # Find the package with the minimum distance
        next_stop, index = next_nearest(truck, graph)

        # Pop the package with the shortest distance
        current_package = truck.truck_content.pop(index)

        # Get the next location pair to pull from the graph
        next_pair = current_package[10], truck.currentLocation

        # Pull the distance (edge weight) of the pair from the graph.
        distance_to_next = graph.edge_weights.get(next_pair)

        # distance_to_next = distance_to_next / 1

        # Add the edge weight to the distance traveled by the truck.
        truck.distance_traveled = truck.distance_traveled + distance_to_next

        # Set the status of the current package to delivered
        # TODO This only updates on board the truck, needs to update the hash table as well.
        current_package[9] = 'delivered'

        # Update the trucks current location to that of the current package.
        truck.currentLocation = current_package[10]

        # Re-compute the package count.
        pc = len(truck.truck_content)

    # Return the truck to the hub.
    # Add the distance from the last stop back to the hub and set the location to the hub.
    truck.distance_traveled = graph.edge_weights.get(truck.currentLocation, 0) + truck.distance_traveled
    truck.currentLocation = 0

    print("Truck", truck.truck_id, "travelled",  round(truck.distance_traveled, 2), "miles.")