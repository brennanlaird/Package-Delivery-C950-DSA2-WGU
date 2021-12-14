import packHash
from packHash import PackageHashTable

def display_main():
    # Text menu that offers choices to the user.
    print("")
    print("-----WGUPS DELIVERY PROGRAM-----")
    print("")
    print("Please select from the following menu options:")
    print("1 - Execute Delivery Program")
    print("2 - View Package Status")
    print("3 - EXIT")


def display_submenu():
    print("")
    print("-----PACKAGE DELIVERY STATUS-----")
    print("")
    print("1 - Search by package ID")
    print("2 - Package status at a time")
    print("3 - Return to main")
    print("4 - Exit")

def submenu_functionality():
    valid = False

    # sub_input = int(input("Enter an option to proceed"))

    while (valid == False):

        sub_input = int(input("Enter an option to proceed"))

        if sub_input == 1:
            valid = True
            search_package = int(input("Enter the package ID."))
            # packHash.PackageHashTable.searchPackage(search_package)
        elif sub_input == 2:
            valid = True
        elif sub_input == 3:
            valid = True
            return False
            # re-launch main
        elif sub_input == 4:
            valid = True
            exit(0)
        else:
            print("Invalid entry, try again")

