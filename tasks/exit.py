"""

Author: Cody Swindells

Created: 06/10/21

Modfied: 14/10/21

Working making addition to add exit from import as small useful project

Higher functions was the solution here.

Completed

"""

class exitProgram:
    """

    Main class to be called to further projects.

    """

    def main(program):
        """
        Main function that will use for further projects
        for loops and exit for console based python projects.

        Higher order functions was solution here.
        """
        exit = ""

        while(exit != "exit"):
            program() #now calls the function
            exit = input("Do you wish to exit program? \n").lower()


