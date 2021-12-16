'''
This code creates the chaining hash table to store each package.
The code was originally pulled from the C950 Zybooks - Section 7.8.
The code was modified to meet the needed functionality and to improve readability.
'''


# HashTable class using chaining.
class PackageHashTable:
    # Constructor with hard coded initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new package into the hash table.
    def insertPackage(self, id, address, city, state, zip, deadline, mass, notes, truck, status, address_id):
        # get the bucket list where this item will go.
        bucket = hash(id) % len(self.table)
        bucket_list = self.table[bucket]

        # Determine if the package ID is in the bucket list already
        for i in bucket_list:
            # Edits each item in the bucket list with the newly passed information IF the item is found in the list.
            if i[0] == id:
                i[1] = address
                i[2] = city
                i[3] = state
                i[4] = zip
                i[5] = deadline
                i[6] = mass
                i[7] = notes
                i[8] = truck
                i[9] = status
                i[10] = address_id
                return True

        # if the id was not found, the information passed in is added to the variable then appended to the bucket list
        new_package = [id, address, city, state, zip, deadline, mass, notes, truck, status, address_id]

        # insert the package to the end of the bucket list.
        bucket_list.append(new_package)

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def searchPackage(self, id):
        # get the bucket list where this key would be.
        bucket = hash(id) % len(self.table)
        bucket_list = self.table[bucket]

        # Iterates over the items in the bucket list
        for package_item in bucket_list:

            # search for the id in the current item
            if id == package_item[0]:
                # return the package object if it is found in the bucket list
                return package_item

        # the key is not found.
        return None

    # Removes an item with matching key from the hash table.
    def removePackage(self, id):
        # get the bucket list where this item will be removed from.
        bucket = hash(id) % len(self.table)
        bucket_list = self.table[bucket]

        # Iterates over the items in the bucket list
        for package_item in bucket_list:
            # search for the id in the current item
            if id == package_item[0]:
                # if the id is found in the current item, remove it
                bucket_list.remove(package_item)

        # the id is not found.
        return None


