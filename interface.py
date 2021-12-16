from datetime import datetime

import packHash
from delivery_main import delivery_main
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

    while valid == False:

        sub_input = int(input("Enter an option to proceed"))

        if sub_input == 1:
            valid = True
            valid = get_package_id()
            if not valid:
                display_submenu()
            return True
        elif sub_input == 2:
            valid = True
            valid = get_time()
            if not valid:
                display_submenu()
            return True
        elif sub_input == 3:
            valid = True
            return False
            # re-launch main
        elif sub_input == 4:
            valid = True
            exit(0)
        else:
            print("Invalid entry, try again")


def get_time():
    valid_entry = False

    while not valid_entry:
        print("")
        print("Enter a time using the following format or x to exit.:")
        print("HH:MM AM/PM   example: 9:45 AM, 12:05 PM")
        user_input = input()

        if user_input == 'x' or user_input == 'X':
            return False

        try:
            user_time = datetime.strptime(user_input, "%I:%M %p")
            valid_entry = True

            delivery_main(user_input, False)
        except ValueError:
            valid_entry = False
            print("Invalid entry. Please try again or type x to exit.")


def get_package_id():
    valid_entry = False

    while not valid_entry:
        print("")
        print("Enter a package ID or x to exit:")
        user_input = input()

        if user_input == 'x' or user_input == 'X':
            return False

        try:
            package_id = int(user_input)

            valid_entry = True

            delivery_main('11:59 PM', False, package_id)
            return True

        except ValueError:
            valid_entry = False
            print("Invalid entry. Please try again or type x to exit.")
