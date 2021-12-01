'''

'''

class Package:
    # Define the package constructor based on the headers from the provided Excel file.
    def __init__(self, id, address, city, state, zip, deadline, mass, notes ):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes

# Any functions go here
