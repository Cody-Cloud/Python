"""
Task: Who's Paying

Author: Cody Swindells

Created: 27/08/21

Modified: 28/08/21

Select a random name from a list created from names separated by a comma


"""

import random

class whoPaying:
    """
    Main object for the program
    """
    
    def select_name():
        """
        
        Parameters:

        none

        Print a name drawn from a list created from a string.
        
        
        """

        names_string = input("Give me everybody's names, separated by a comma. ")

        names = names_string.split(",")

        print(names[random.randint(0, len(names)-1)])

whoPaying.select_name()