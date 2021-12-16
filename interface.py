from datetime import datetime
from delivery_main import delivery_main


# Time Complexity O(1)  Space Complexity O(1)
def display_main():
    # Text menu that offers choices to the user.
    print("")
    print("-----WGUPS DELIVERY PROGRAM-----")
    print("")
    print("Please select from the following menu options:")
    print("1 - Execute Delivery Program")
    print("2 - View Package Status")
    print("3 - EXIT")


# Time Complexity O(1)  Space Complexity O(1)
def display_submenu():
    # Text menu that offers choices to the user for the submenu.
    print("")
    print("-----PACKAGE DELIVERY STATUS-----")
    print("")
    print("1 - Search by package ID")
    print("2 - Package status at a time")
    print("3 - Return to main")
    print("4 - Exit")


# Function to take user input from the CL and implement the sub menu functionality.
# Time Complexity O(n)  Space Complexity O(1)
def submenu_functionality():
    # Set valid to false to loop through an obtain a valid user input.
    valid = False

    # While the user has not provided a valid input
    while not valid:
        try:
            # Display a prompt and try to convert user input to an integer.
            sub_input = int(input("Enter an option to proceed"))

            # For user input of 1 to search by package ID.
            if sub_input == 1:
                valid = True
                # Determine a valid entry by the return from the get_package_id function.
                valid = get_package_id()
                # If the return is not valid, re-display the menu and call the functionality again.
                if not valid:
                    display_submenu()
                    submenu_functionality()
                return True
            # For user input of 2 to display all packages at a given time.
            elif sub_input == 2:
                valid = True
                # Determine a valid entry by the return from the get_time function.
                valid = get_time()
                # If the return is not valid, re-display the menu and call the functionality again.
                if not valid:
                    display_submenu()
                    submenu_functionality()
                return True
            # For user input of 3 to return to the main menu.
            elif sub_input == 3:
                valid = True
                # Re-display the main menu and return false to re-start the while loop that finds a valid user entry.
                display_main()
                return False
            # For user input of 4 to exit the program.
            elif sub_input == 4:
                valid = True
                exit(0)
            # Displays an invalid integer entry and re-displays the sub menu options.
            else:
                print("Invalid entry, try again")
                print("")
                display_submenu()
        # Except catches a non-integer invalid entry and re-displays the sub menu options.
        except ValueError:
            print("Invalid entry, try again")
            print("")
            display_submenu()


# Function to get a time input by the user inorder to display package status at that time.
# Time Complexity O(n)  Space Complexity O(1)
def get_time():
    # Sets valid input as false to loop until a valid entry is input
    valid_entry = False
    # Loop to check for a valid user input
    while not valid_entry:
        # Prompts the user to enter a time and or an exit character.
        print("")
        print("Enter a time using the following format or x to exit.:")
        print("HH:MM AM/PM   example: 9:45 AM, 12:05 PM")
        # Gets the user input
        user_input = input()

        # if the user enters an x then false is returned to the calling code.
        if user_input == 'x' or user_input == 'X':
            return False

        # Try to parse the user input to a date time object. If this is successful, valid entry is set to true.
        try:
            user_time = datetime.strptime(user_input, "%I:%M %p")
            valid_entry = True
            # On a valid entry, the user input is set as the time and the main delivery code is executed
            # up to that time. Display results parameter is set to false.
            delivery_main(user_input, False)
        # On a value error the prompt is re-displayed to get a valid time.
        except ValueError:
            valid_entry = False
            print("Invalid entry. Please try again or type x to exit.")


# Function to get a specific package id from the user.
# Time Complexity O(n)  Space Complexity O(1)
def get_package_id():
    # Sets valid input as false to loop until a valid entry is input
    valid_entry = False
    # Loop to check for a valid user input
    while not valid_entry:
        # Prompt the user to enter an id or exit code.
        print("")
        print("Enter a package ID or x to exit:")
        user_input = input()

        # if the user enters an x then false is returned to the calling code.
        if user_input == 'x' or user_input == 'X':
            return False

        # Try to convert the user input to an integer.
        try:
            package_id = int(user_input)
            # Change valid entry to true to break while loop.
            valid_entry = True
            # Run the main delivery code to the end of day and pass the entered package id.
            delivery_main('11:59 PM', False, package_id)
            return True
        # Except catches non-integer entries and re-displays the prompt.
        except ValueError:
            valid_entry = False
            print("Invalid entry. Please try again or type x to exit.")
