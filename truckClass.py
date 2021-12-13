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

    # truck_packages = []
    while pc < truck.capacity:
        # TODO Change the status of the loaded package in the hash table when it is loaded.
        truck.truck_content.append(PackageHashTable.searchPackage(pack_table, pc + 1))
        pc += 1


def deliver_packages(truck, graph):
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

    print("Truck", truck.truck_id, "travelled", round(truck.distance_traveled, 2), "miles.")
    print("Truck", truck.truck_id, " took", round(truck.distance_traveled / truck.speed, 2), "hours")


# Defines a manual scheme for loading trucks.
def manual_load_truck(pack_table, pc):
    current_id = 1

    truck_loading = [2, 2, 2, 1, 2, 2, 1, 1, 3, 2, 2, 3, 1, 1, 1, 1, 3, 2, 1, 1, 1, 3, 3, 3, 2, 2, 3, 2, 1, 1, 1, 2, 2,
                     1, 3, 2, 2, 2, 1, 1]

    while current_id <= pc:
        current_package = PackageHashTable.searchPackage(pack_table, current_id)

        current_package[8] = truck_loading[current_id - 1]

        PackageHashTable.insertPackage(pack_table, current_package[0], current_package[1],
                                       current_package[2], current_package[3], current_package[4],
                                       current_package[5], current_package[6], current_package[7],
                                       current_package[8], current_package[9], current_package[10])

        current_id += 1

def manual_distribute(truck, pack_table, package_count):
    # Counts how many packages are loaded onto the truck.
    loaded_count = 0

    # List for debugging
    truck_packages = []

    current_id = 1

    while current_id <= package_count:
        current_package = PackageHashTable.searchPackage(pack_table, current_id)
        if current_package[8] == truck.truck_id:
            truck.truck_content.append(current_package)
            loaded_count += 1
        current_id += 1
    '''
    
    while pc < truck.capacity:
        # TODO Change the status of the loaded package in the hash table when it is loaded.

        if PackageHashTable.searchPackage(pack_table, pc + 1)[8] == truck.truck_id:
            truck.truck_content.append(PackageHashTable.searchPackage(pack_table, pc + 1))
            truck_packages.append(PackageHashTable.searchPackage(pack_table, pc + 1))
        # truck.truck_content.append(PackageHashTable.searchPackage(pack_table, pc + 1))
            pc += 1
        if PackageHashTable.searchPackage(pack_table, pc + 1)[0] == package_count:
            pc = truck.capacity
    
    '''