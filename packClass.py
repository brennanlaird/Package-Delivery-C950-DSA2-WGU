
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


def package_print(packtable):
    pc = 1
    while pc < 41:
        print(packtable.searchPackage(pc))
        pc += 1
