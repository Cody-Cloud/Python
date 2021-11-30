"""

Author: Cody Swindells

Created: 10/10/21

Modified: 30/11/21

Task to created a strong password generator

#BUGFIX - list indices must be intergers or slices, not tuple - line 44

#BUGFIX - unexpected outcome - not generating password with all count of each selection.

Now works.

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
        nr_letters = int(input(f"How many letters would you like in your password?\n")) 
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

        total_length =  nr_letters + nr_symbols + nr_numbers

        random_select = 0

        passwordStr = ""

        while((nr_symbols > 0) or (nr_letters > 0) or (nr_numbers > 0)):
            # or logical operator works via this method.
            random_select = random.randint(1, 3)
            if (random_select == 1):
                if(nr_letters > 0):
                    passwordStr += passGen.letters[random.randint(0, len(passGen.letters)-1)]
                    nr_letters -= 1
                else:
                    continue
            elif (random_select == 2):
                if(nr_numbers > 0):
                    passwordStr += passGen.numbers[random.randint(0, len(passGen.numbers)-1)]
                    nr_numbers -= 1
                else:
                    continue
            elif (random_select == 3):
                if(nr_symbols > 0):
                    passwordStr += passGen.symbols[random.randint(0, len(passGen.symbols)-1)]
                    nr_symbols -= 1
                else:
                    continue

        print(f"This is your new password {passwordStr}.\n")

passGen.passMain()