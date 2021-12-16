
# Student: Brennan Laird
# WGU ID#: 001415733

# FULL PROGRAM
# Time Complexity O(n^2)  Space Complexity O(n)

from delivery_main import delivery_main
from interface import display_main, display_submenu, submenu_functionality

if __name__ == '__main__':

    # Displays the main menu.
    display_main()

    # Sets valid input to false to loop until a valid entry is input
    valid_input = False

    # Loop to check for a valid user input
    # Time Complexity O(n)  Space Complexity O(1)
    while not valid_input:
        # try to convert the user input to an integer. If this works it loops through the menu functionality.
        try:
            # Gets the users input from the console and converts it to an integer.
            main_menu_input = int(input("Enter the number to proceed with the menu choice."))

            # If the input is 1 then run the main delivery program.
            if main_menu_input == 1:
                # Runs the main delivery program with default values and sets valid input to true.
                valid_input = True
                delivery_main()
                # Exits the program after this is run.
                exit(0)
            elif main_menu_input == 2:
                # launch the sub menu
                display_submenu()
                # Valid input is determined based on the return value of the submenu function.
                valid_input = submenu_functionality()

            elif main_menu_input == 3:
                # Exits the program.
                valid_input = True
                exit(0)
            else:
                # Flags an invalid input and re-displays the main menu.
                print("Invalid input, try again.")
                print("")
                # Re-displays the main menu on invalid input.
                display_main()
                # Gets the users input from the console.

        # Except statement catches non-integer input and flags it as invalid.
        except ValueError:
            valid_entry = False
            # Flags an invalid input and re-displays the main menu.
            print("Invalid input, try again.")
            print("")
            # Re-displays the main menu on invalid input.
            display_main()
            # Gets the users input from the console.
