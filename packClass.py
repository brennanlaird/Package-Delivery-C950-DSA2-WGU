class Package:
    # Define the package constructor based on the headers from the provided Excel file.
    # Additional parameters are for the truck to load the package, delivery status, and address ID.
    def __init__(self, id, address, city, state, zip, deadline, mass, notes, truck, status, address_id):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.truck = truck
        self.status = status
        self.address_id = address_id


# Function to print each package in the table.
# Time Complexity O(n)  Space Complexity O(1)
def package_print(packtable):
    # Set package id to 1.
    p_id = 1
    # Loop through each package of the 40 package ids.
    while p_id < 41:
        # Search the hash table for the id and print the results.
        print(packtable.searchPackage(p_id))
        p_id += 1
