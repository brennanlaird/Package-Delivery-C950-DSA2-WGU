'''
Student: Brennan Laird
WGU ID#: 001415733
'''

import csv

from testCode import *  # Code to test program functionality

if __name__ == '__main__':

    # Creates a new empty package hash table.
    packageTable = PackageHashTable()

    # Variable to keep track of the package count. Used for iterating through the packages.
    pc = 0

    # Open and read the package file.
    with open('WGUPS Package File.csv', 'r') as csv_file:
        package_data = csv.reader(csv_file)

        # Skips the initial header line in the csv
        next(package_data)

        # For each line in the CSV, create a new package object and store it in the hash table.
        for line in package_data:
            # Creates a temporary package object from each line of the file.
            # Additional default values are included at the end for the package object.
            temp_package = Package(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], 0, 0, -1)

            # Converts the package id from a string to an integer value.
            # The conversion resulted in more predictable hashing and improved the ability to search.
            temp_package.id = int(temp_package.id)

            # Insert the temporary package into the hash table.
            packageTable.insertPackage(temp_package.id, temp_package.address,
                                       temp_package.city, temp_package.state, temp_package.zip,
                                       temp_package.deadline, temp_package.mass, temp_package.notes,
                                       temp_package.truck, temp_package.status, temp_package.address_id)
             # Increment the package count by 1.
            pc += 1

    # Create a new graph structure to store the distance table
    graphSLC = Graph()

    # Open and read the distance file.
    with open('WGUPS Distance Table.csv', 'r') as csv_file:
        distance_data = csv.reader(csv_file)

        # Skips the initial header line in the csv
        next(distance_data)

        # Creates a new empty dictionary object to store the information from the distance csv
        distance_dict = {}

        # Sets up a blank distance table to store the distances
        # Items will be indexed based on the address ID pulled from the CSV
        distance_table = []

        # Sets the initial address ID to zero
        address_id = 0

        # This iterates over each line of the distance data  and adds the information to the appropriate data structure
        for line in distance_data:
            # Adds the current item to the dictionary with the address ID as key and Name and values as a sub-dictionary
            distance_dict[address_id] = {'Name': line[0], 'Address': line[1]}

            # Adds a vertex to the graph that has the address ID
            graphSLC.add_vertex(address_id)

            # Creates a temporary list item to store the distances from the CSV file
            temp_list = []

            # Add each item in the line to the temporary list
            for i in line:
                temp_list.append(i)

            # Removes the first two items from the temporary list.
            temp_list.pop(0)
            temp_list.pop(0)

            # Adds the temporary list the full distance table.
            distance_table.append(temp_list)

            # Increments the address ID for the next loop iteration
            address_id += 1

    # Set of nested for loops to read the information stored in the distance table list
    # and create undirected graph edges.

    # The distance table is a list of lists and thus the first for loop iterates through each outer item.
    for outer_item in distance_table:
        # Get the index
        outer_index = distance_table.index(outer_item)

        # This index is used to track the index on the inner list in the distance table.
        # The inner index is reset to zero each time a new outer item is iterated over.
        inner_index = 0

        # Each inner list is iterated over to read the item stored.
        # If the item is a valid distance, and undirected graph edge is created.
        for inner_item in distance_table[outer_index]:

            # Create a new edge if the distance is not blank
            if distance_table[outer_index][inner_index] != '':
                graphSLC.add_undirected_edge(outer_index, inner_index, float(distance_table[outer_index][inner_index]))

            # Increment the inner index counter.
            inner_index += 1

    # This code iterates through each package in the hash table to modify the address ID
    # The address associated with the package is compared with the address in the distance dictionary.
    # When a matching address is found, the address ID of the package is updated.

    # i is the counter for the while loop
    i = 1

    # while the counter is less than the total package count, retrieve the current package.
    while i <= pc:
        current_package = packageTable.searchPackage(i)

        # Search through the dictionary to find the address associated with the package.
        for key in distance_dict:

            # if the address from the package is found, update the address id for the package and break the loop.
            if current_package[1] in distance_dict[key]['Name']:
                current_package[10] = key
                break
            if current_package[1] in distance_dict[key]['Address']:
                current_package[10] = key
                break
        i += 1

    # Executes the manual load scheme on the packages by assigning the predefined truck ID to the package ID.
    manual_load_truck(packageTable, pc)

    # Define a new truck with ID 1, located at the hub, with an average speed of 18 mph, and capacity of 16 packages.
    truck1 = Truck(1, 0, 18, 16, [], 0)
    truck2 = Truck(2, 0, 18, 16, [], 0)
    truck3 = Truck(3, 0, 18, 16, [], 0)

    manual_distribute(truck1, packageTable, pc)
    manual_distribute(truck2, packageTable, pc)
    manual_distribute(truck3, packageTable, pc)

    # for item in truck3.truck_content:
        # print(item)

    # load_truck(truck1, packageTable)
    # load_truck(truck2, packageTable)
    # load_truck(truck3, packageTable)

    # print(truck1.truck_content)

    deliver_packages(truck1, graphSLC)
    deliver_packages(truck2, graphSLC)
    deliver_packages(truck3, graphSLC)

    # Test code to verify program functionality.
    # Called from functions written in the test code module.

    # Testing the package loading code
    # package_deadline(packageTable,pc)

    # manual_load_truck(packageTable, pc)

    # Check the edges and adjacency lists
    # graph_print(graphSLC)

    # Print the address dictionary one line at a time.
    # dictionary_print(distance_dict)

    # Prints out the full package table one line at a time.
    # package_print(packageTable)

    # print(minDist(graphSLC, distance_dict, 5))

    # lookUp(distance_table,distance_dict,8,9)

    # lookUp(distance_table,distance_dict,9,1)

    # lookUp(distance_table,distance_dict,4,15)

    # lookUp(distance_table,distance_dict,6,6)
