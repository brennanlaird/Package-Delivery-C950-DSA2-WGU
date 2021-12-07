
from packHash import *
from packClass import *


class Truck:
    # Define the truck object constructor.
    def __init__(self, truck_id, currentLocation, speed, capacity, truck_content):
        self.truck_id = truck_id
        self.currentLocation = currentLocation
        self.speed = speed
        self.capacity = capacity
        self.truck_content = []


# Any functions go here
def load_truck(truck, pack_table):
    pc = 0
    truck_packages = []
    while pc < truck.capacity:
        #truck_packages.append(pack_table.searchPackages(pc+1))
        truck.truck_content.append(PackageHashTable.searchPackage(pack_table,pc+1))
        #print(PackageHashTable.searchPackage(pack_table,pc+1))
        pc += 1

def deliver_packages(truck, distance_dict):
    print("Drive around")
    pc = len(truck.truck_content)
    while pc > 0:
        # Pop the package
        current_package = truck.truck_content.pop(0)
        # print(current_package)

        # Read the package address
        next_stop = current_package[1]

        print("Next stop: ", next_stop)

        # Find the vertex that has the same address
        addID=-1
        for key in distance_dict:
            if distance_dict.get(key) == next_stop:
                addID = key
                break
        print(addID)

        # Travel to that vertex
        # Update the trucks current location

        pc = len(truck.truck_content)
