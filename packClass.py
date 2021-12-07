'''

'''


class Package:
    # Define the package constructor based on the headers from the provided Excel file.
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


# Any functions go here
def add_address_id(dictionary, package, pc):
    i = 1
    while i <= pc:
        current_package = package.searchPackage(i)

        for key in dictionary:

            if current_package[1] in dictionary[key]['Name']:
                current_package[10] = key
        i += 1
