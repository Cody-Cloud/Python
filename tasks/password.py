"""

Author: Cody Swindells

Created: 10/10/21

Modified: 11/10/21

Task to created a strong password generator

#BUGFIX - list indices must be intergers or slices, not tuple - line 44

#BUG - unexpected outcome - not generating password with all count of each selection.

"""

import random

class passGen:
    """
    Main class object

    Contains some base starter code with modification
    """

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def passMain():
        """
        Main function of the program

        Prints password that is generatered based of user input.
        """
        print("Welcome to the PyPassword Generator!")
        nr_letters= int(input(f"How many letters would you like in your password?\n")) 
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

        total_length =  nr_letters + nr_symbols + nr_numbers

        passwordStr = ""

        for i in range(total_length):
            # i will be become too large, will have to rethink the logic at play
            if (nr_letters >= 0):
                passwordStr += passGen.letters[random.randint(0, len(passGen.letters))]
            if (nr_numbers >= 0):
                passwordStr += passGen.numbers[random.randint(0, len(passGen.numbers))]
            if (nr_symbols >= 0):
                passwordStr += passGen.symbols[random.randint(0, len(passGen.symbols))]
            nr_letters -= i
            nr_numbers -= i
            nr_symbols -= i
        print(f"This is your new password {passwordStr}.\n")

passGen.passMain()