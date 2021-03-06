import csv
import packClass
from graphClass import *
from truckClass import *


# The main delivery function. It can take several parameters that allow it to display results in different ways.
# The end time is a string that is parsed into a datetime. This allows the function to stop running and display results
# at a user specified time. Display results will cause the full package table to display. The get id parameter will
# display the results of a single package if it is not 0.
# Time Complexity O(n^2)  Space Complexity O(n)
def delivery_main(endtime='11:59 PM', display_results=True, get_id=0):
    # Creates a new empty package hash table.
    packageTable = PackageHashTable()

    # Variable to keep track of the package count. Used for iterating through the packages.
    pc = 0

    # Open and read the package csv file.
    # Time Complexity O(n)  Space Complexity O(n)
    with open('WGUPS Package File.csv', 'r') as csv_file:
        package_data = csv.reader(csv_file)

        # Skips the initial header line in the csv
        next(package_data)

        # For each line in the CSV, create a new package object and store it in the hash table.
        for line in package_data:
            # Creates a temporary package object from each line of the file.
            # Additional default values are included at the end for the package object.
            temp_package = packClass.Package(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], 0,
                                             0, -1)

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
    # Time Complexity O(n^2)  Space Complexity O(n)
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
    # Time Complexity O(n^2)  Space Complexity O(n)
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
    # Time Complexity O(n^2)  Space Complexity O(n)
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

    # Define a new truck with ID number, located at the hub, with an average speed of 18 mph,
    # and capacity of 16 packages. The empty list will hold packages, the distance travelled is set to zero.
    # The time is a string that represents the time the truck leaves the hub.
    truck1 = Truck(1, 0, 18, 16, [], 0, '8:00 AM')
    truck2 = Truck(2, 0, 18, 16, [], 0, '9:05 AM')
    truck3 = Truck(3, 0, 18, 16, [], 0, '10:20 AM')

    # Calls the manual distribute function to distribute the packages to their respective trucks.
    manual_distribute(truck1, packageTable, pc)
    manual_distribute(truck2, packageTable, pc)
    manual_distribute(truck3, packageTable, pc)

    # Executes the deliver packages function for truck 1.
    deliver_packages(truck1, graphSLC, packageTable, endtime)

    # Change the status of the delayed packages to loaded if the time is past the delayed arrival time.

    # Converts end time parameter to date time object.
    end_time = datetime.strptime(endtime, "%I:%M %p")
    delay_time = datetime.strptime('9:05 AM', "%I:%M %p")

    # If the end time is after the delayed time then the delayed packages will have arrived.
    # Time Complexity O(n)  Space Complexity O(n)
    if end_time >= delay_time:
        # Change the delayed packages' status to loaded if they have arrived.
        # Start at package id 1
        i = 1
        # While package id is less than the package count.
        while i <= pc:
            # Get the package id from the hash table.
            current_package = packageTable.searchPackage(i)
            # If the note field contains delayed, adjust the status to show it has arrived and was loaded.
            if search('Delayed', current_package[9]):
                current_package[9] = 'At Hub - Loaded on delivery vehicle'
            i += 1

    # Execute the deliver packages function for truck 2.
    deliver_packages(truck2, graphSLC, packageTable, endtime)

    # Updates the address for package #9 to correct address if the time is past 10:20 AM.
    change_time = datetime.strptime('10:20 AM', "%I:%M %p")

    if end_time >= change_time:
        # Finds the package ID in the hash table
        update_package = packageTable.searchPackage(9)

        # Updates the package address fields.
        update_package[1] = '410 S State St'
        update_package[2] = 'Salt Lake City'
        update_package[3] = 'UT'
        update_package[4] = '84111'
        update_package[7] = 'Address corrected'

        # Search through the dictionary to find the address associated with the package to be updated.
        # Time Complexity O(n)  Space Complexity O(n)
        for key in distance_dict:

            # if the address from the package is found, update the address id for the package and break the loop.
            if update_package[1] in distance_dict[key]['Name']:
                update_package[10] = key
                break
            if update_package[1] in distance_dict[key]['Address']:
                update_package[10] = key
                break

        # Updates the packages in the hash table.
        packageTable.insertPackage(update_package[0], update_package[1], update_package[2], update_package[3],
                                   update_package[4], update_package[5], update_package[6], update_package[7],
                                   update_package[8], update_package[9], update_package[10])

    # Update truck 3 departure time to the time that the first truck returns to the hub.
    # This accounts for only having two drivers.
    next_departure = min(truck1.truck_time, truck2.truck_time)

    # If the next departure is after the designated departure time for truck 3, reset the truck 3 time to later.
    if next_departure > datetime.strptime(truck3.truck_time, "%I:%M %p"):
        truck3.truck_time = next_departure.strftime("%I:%M %p")

    # Execute the deliver packages function for truck 3.
    deliver_packages(truck3, graphSLC, packageTable, endtime)

    # Find the time the last truck returns to the hub.
    end_time = max(truck1.truck_time, truck2.truck_time, truck3.truck_time)

    # Find the total distance that the trucks travelled.
    total_distance = truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled

    # if display results is true, show the final totals.
    if display_results is True:
        print("")
        print("----FINAL RESULT----")
        print("Total Distance Travelled: ", round(total_distance, 2), "miles")
        print("Day finished at ", end_time.strftime("%I:%M %p"))

    # If display results is false and there is no specific package id, display the full package table.
    if display_results is False and get_id == 0:
        # Print a header and the time.
        print("Package Table at", endtime)
        # Print the table one line at a time with the package_print function.
        packClass.package_print(packageTable)

    # if there is a specific package, look for it in the hash table and display the output.
    if get_id != 0:
        # Search for the package in the table.
        display_package = packageTable.searchPackage(get_id)
        # Display the results if found.
        if display_package is not None:
            print("Package ID:", display_package[0])
            print("Address:", display_package[1], "  ", display_package[2], ",", display_package[3], " ",
                  display_package[4])
            print("Delivery Deadline: ", display_package[5])
            print("Weight: ", display_package[6])
            print("Status: ", display_package[9])
        # Display the results if nothing is found.
        else:
            print("Package", get_id, "was not found.")
