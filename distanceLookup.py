from datetime import datetime


# This code finds the nearest vertex to the current truck location using a nearst neighbor algorithm.
# It first defines the next soonest delivery time found in the truck and among packages due to be delivered soonest,
# the algorithm finds the next shortest distance.
# Time Complexity O(n)  Space Complexity O(1)
def next_nearest(truck, graph):
    # Sets up the minimum as an arbitrary high value and sets the current location to the location of the truck.
    min = 1000
    current_loc = truck.currentLocation

    # Sets the minimum time to end of day. This will find the earliest delivery time.
    min_time = datetime.strptime('11:59 PM', "%I:%M %p")

    # Finds the minimum delivery time for the packages on the truck.
    # This is used to prioritise the deadline first.
    # Time Complexity O(n)  Space Complexity O(1)
    for package in truck.truck_content:
        # Gets the deadline of the package as a string.
        time_string = package[5]

        # If the deadline string is end of day (EOD) it is changed to a time value at the EOD
        if time_string == 'EOD':
            time_string = '11:59 PM'
        # The string is converted to a datetime object.
        next_deadline = datetime.strptime(time_string, "%I:%M %p")

        # If the deadline is less than the minimum, set it to the minimum.
        if next_deadline < min_time:
            min_time = next_deadline

    # For loop finds the minimum next distance among all the packages loaded on the truck.
    # Time Complexity O(n)  Space Complexity O(1)
    for package in truck.truck_content:
        # Pull the next address index from the current package.
        next_location = package[10]

        # Gets the deadline of the package as a string.
        time_string = package[5]

        # If the deadline string is end of day (EOD) it is changed to a time value at the EOD
        if time_string == 'EOD':
            time_string = '11:59 PM'
        # The string is converted to a datetime object.
        next_deadline = datetime.strptime(time_string, "%I:%M %p")

        # x represents a tuple of the current and next location that is then pulled from the graph edge weights.
        x = current_loc, next_location
        next_distance = graph.edge_weights.get(x)

        # If the next distance is less than the minimum, set that to be the next location to deliver to if the
        # next deadline is equal to the minimum. This allows for both time and distance to be considered.
        if next_distance < min and next_deadline == min_time:
            min = next_distance
            next_stop = next_location
            # Gets the index location of the current package in the truck.
            index = truck.truck_content.index(package)
    # Returns the trucks next stop and the index location of the package
    return next_stop, index
