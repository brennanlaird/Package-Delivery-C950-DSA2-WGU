'''
Student: Brennan Laird
WGU ID#: 001415733
'''

import csv
import packHash
import packClass

if __name__ == '__main__':
    print("Here we go...")

    # Creates a new empty package hash table.
    packageTable = packHash.PackageHashTable()

    # Open and read the package file.
    with open('WGUPS Package File.csv', 'r') as csv_file:
        package_data = csv.reader(csv_file)

        # Skips the initial header line in the csv
        next(package_data)

        # For each line in the CSV, create a new package object and store it in the hash table.
        for line in package_data:
            '''
            1 - Store the line data as a temporary object
            2 - Add that temp object to the hash table
            '''
            temp_package = packClass.Package(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])

            packHash.PackageHashTable.insertPackage(packageTable, temp_package)
            #print(packageTable.table)
            #print(line)
        print(packageTable.table)

        print(packageTable.search(temp_package))