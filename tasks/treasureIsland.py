
"""
Author: Cody Swindells

Created: 29/09/21

Modified: 30/09/21


"""
class treasureStarter:
    """
    Based code required for the code challenge from the course

    Below based partly from replit 4.3 Excerise and modified by me.
    """
    row1 = ["⬜️","⬜️","⬜️"]
    row2 = ["⬜️","⬜️","⬜️"]
    row3 = ["⬜️","⬜️","⬜️"]
    map = [row1, row2, row3]
    def initialise():
        print(f"{treasureStarter.row1}\n{treasureStarter.row2}\n{treasureStarter.row3}\n")
        

class treasureIsland:
    """
    
    Main Object of the main program.

    My own work towards the coding challenge.

    Attempting to use recursion to deal with
    the issue of user input generating errors.

    Parameters:

    None

    Returns:
    
    None

    Output:

    Prints a grid of 3 by 3 square with one X
    
    """
    def main():
        x = "❌"
        position = input("Where do you want to put the treasure? ")
        map = treasureStarter.map
        if(len(position) == 1):
            treasureIsland.main()
        else:
            if(int(position[0]) < len(map[0])-1 or int(position[1]) < len(map[0])-1):
                map[int(position[0])][int(position[1])] = x
                print(f"{map[0]}\n{map[1]}\n{map[2]}")
            else:
                treasureIsland.main()
treasureStarter.initialise()
treasureIsland.main()