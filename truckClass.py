from datetime import timedelta, datetime
from re import search

import status_output
from distanceLookup import next_nearest
from packHash import *
from packClass import *


class Truck:
    # Define the truck object constructor.
    def __init__(self, truck_id, currentLocation, speed, capacity, truck_content, distance_traveled, truck_time):
        self.truck_id = truck_id
        self.currentLocation = currentLocation
        self.speed = speed
        self.capacity = capacity
        self.truck_content = []
        self.distance_traveled = distance_traveled
        self.truck_time = truck_time


def deliver_packages(truck, graph, pack_table, endtime):
    # Package count is based on the length of the truck content list.
    pc = len(truck.truck_content)

    # Sets the current time to the base time from the truck object and converts it to a datetime object.
    current_time = datetime.strptime(truck.truck_time, "%I:%M %p")

    # Convert the endtime parameter into a datetime object to conduct comparisons.
    end_time = datetime.strptime(endtime, "%I:%M %p")

    # If the current time is greater than the end time parameter, return to the main delivery function.
    if current_time >= end_time:
        # Sets the truck time to the current time. Ensures the truck time is a datetime object.
        truck.truck_time = current_time
        return

        # Current package counter to iterate through items
    cp = 0

    # Updates the package status to out for delivery when the truck leaves the hub.
    for package in truck.truck_content:

        # Get the most current package information from the hash table.
        package = pack_table.searchPackage(package[0])

        # Update the package status.
        package[9] = 'Out for delivery'

        # Updates the truck content  with the latest info from the hash table.
        # This ensures any address corrections are accounted for in the nearest neighbor delivery algorithm.
        for i in range(10):
            truck.truck_content[cp][i] = package[i]

        # Insert the updated status back into the hash table.
        pack_table.insertPackage(package[0], package[1], package[2], package[3], package[4], package[5], package[6],
                                 package[7], package[8], package[9], package[10], )
        cp += 1

    while pc > 0:
        # Find the package with the  next soonest delivery time and minimum distance.
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

        # Update the truck time
        # Computes travel time in hours.
        travel_time = distance_to_next / truck.speed

        # Sets the current time based on the travel time. Travel time is converted into minutes.
        current_time = current_time + timedelta(minutes=travel_time * 60)

        # Triggers a function to print the package status to a file at a given time.
        # Hard codes trigger times based on the performance assessment rubric.
        # Section G1 - Time between 8:35 and 9:25 AM
        trigger_time1 = datetime.strptime('8:45 AM', "%I:%M %p")

        # Section G2 - Time between 9:35 and 10:25 AM
        trigger_time2 = datetime.strptime('9:45 AM', "%I:%M %p")

        # Section G3 - Time between 12:03 and 1:12 PM
        trigger_time3 = datetime.strptime('12:10 PM', "%I:%M %p")

        temp_truck_time = current_time - timedelta(minutes=travel_time * 60)
        # print(type(truck.truck_time))

        # if the current time passes the desired end time then return to the calling function.
        if current_time >= end_time > temp_truck_time:
            print("This triggered")
            return

        if current_time >= trigger_time1 > temp_truck_time:
            status_output.print_status(current_time, pack_table, truck, trigger_time1, trigger_time2, trigger_time3)

        if current_time >= trigger_time2 > temp_truck_time:
            status_output.print_status(current_time, pack_table, truck, trigger_time1, trigger_time2, trigger_time3)

        if current_time >= trigger_time3 > temp_truck_time:
            status_output.print_status(current_time, pack_table, truck, trigger_time1, trigger_time2, trigger_time3)

        # Sets the truck time to match the current time.
        truck.truck_time = current_time

        # Set the status of the current package to delivered
        current_package[9] = 'delivered at ' + current_time.strftime("%I:%M %p")

        # Updates the delivery status in the hash table.
        pack_table.insertPackage(current_package[0], current_package[1], current_package[2], current_package[3],
                                 current_package[4], current_package[5], current_package[6], current_package[7],
                                 current_package[8], current_package[9], current_package[10])

        # Update the trucks current location to that of the current package.
        truck.currentLocation = current_package[10]

        # Re-compute the package count.
        pc = len(truck.truck_content)

    # Return the truck to the hub.
    # Add the distance from the last stop back to the hub and set the location to the hub.
    truck.distance_traveled = graph.edge_weights.get(truck.currentLocation, 0) + truck.distance_traveled
    truck.currentLocation = 0

    # Update the truck time
    # Computes travel time in hours.
    travel_time = graph.edge_weights.get(truck.currentLocation, 0) / truck.speed

    # Sets the current time based on the travel time. Travel time is converted into minutes.
    current_time = current_time + timedelta(minutes=travel_time * 60)
    truck.truck_time = current_time

    # print("Truck", truck.truck_id, "travelled", round(truck.distance_traveled, 2), "miles.")


# Defines a manual scheme for loading trucks.
def manual_load_truck(pack_table, pc):
    # Set the current id to 1, the first package in the list.
    current_id = 1

    # Truck loading scheme determined by the programmer. This is included here to avoid modifying the CSV
    # file.
    truck_loading = [2, 2, 2, 1, 2, 2, 1, 1, 3, 2, 2, 3, 1, 1, 1, 1, 3, 2, 1, 1, 1, 3, 3, 3, 2, 2, 3, 2, 1, 1, 1, 2, 2,
                     1, 3, 2, 2, 2, 1, 1]

    # While the current ID is less than the package count.
    while current_id <= pc:
        # Gets the current ID from the hash table and stores the list as the current package.
        current_package = PackageHashTable.searchPackage(pack_table, current_id)

        # Sets the truck ID from the truck loading scheme based on the index of that list.
        current_package[8] = truck_loading[current_id - 1]

        # Sets the package status.
        if search('Delayed', current_package[7]):
            current_package[9] = 'Delayed'
        else:
            current_package[9] = 'At Hub - Loaded on delivery vehicle'

        # Updates the package in the hash table.
        PackageHashTable.insertPackage(pack_table, current_package[0], current_package[1],
                                       current_package[2], current_package[3], current_package[4],
                                       current_package[5], current_package[6], current_package[7],
                                       current_package[8], current_package[9], current_package[10])
        # Increments the package id for the while loop
        current_id += 1


# Distributes the packages to the trucks content lists.
def manual_distribute(truck, pack_table, package_count):
    # Counts how many packages are loaded onto the truck.
    loaded_count = 0

    # Set the current id to 1, the first package in the list.
    current_id = 1

    # While the current package id is less than the total package count.
    while current_id <= package_count:
        # Gets the current ID from the hash table and stores the list as the current package.
        current_package = PackageHashTable.searchPackage(pack_table, current_id)
        # If the current package is supposed to be on the current truck, add that package to the trucks content list.
        if current_package[8] == truck.truck_id:
            truck.truck_content.append(current_package)
            loaded_count += 1
        current_id += 1
