"""

Author: Cody Swindells

Created: 01/10/21

Modified: 04/10/21

#BUGFIX

Completed

"""

import random

class rockStarter:
    """
    Reworked starter code to suit the object oritentated style of programming.

    Some added was the idea to use nested tuples
    """

    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    game = [(rock, "rock"), (paper, "paper"), (scissors, "scissors")] #nested tuples i.e immutable arrays or lists 


class rock:
    """
    #Main class object from the rock paper
    """
    def user():
        user_select = input("Please make a choice. Either rock, paper or scissors. \n")
        return user_select

    def main(user_select):
        """
        Main function which contains all 
        
        """
        computer_select = random.randint(0, 2)
        if(computer_select == 0 and rockStarter.game[1][1] == user_select):
            print(f"Player selected {user_select}.\n")
            print(rockStarter.game[1][0]) 
            print(f"Computer selected {rockStarter.game[0][1]}.\n")
            print(rockStarter.game[0][computer_select])
            print("Player wins!")
        elif(computer_select == 1 and rockStarter.game[2][1] == user_select):
            print("Player selected .\n")
            print(rockStarter.game[2][0])
            print(f"Computer selected {rockStarter.game[1][1]}.\n")
            print(rockStarter.game[0][computer_select])
            print("Player wins!")
        elif(computer_select == 2 and rockStarter.game[0][1] == user_select):
            print(f"Player selected {user_select}.\n")
            print(rockStarter.game[0][0])
            print(f"Computer selected {rockStarter.game[2][1]}.")
            print(rockStarter.game[computer_select][0])
            print("Player wins!")
        elif(rockStarter.game[computer_select][1] == user_select):
            print(f"Both player and Computer Select {user_select}")
            print(rockStarter.game[computer_select][0]) 
            print("It's a draw!")
        else:
            print(f"Computer selectes {rockStarter.game[computer_select][1]}")
            print(rockStarter.game[computer_select][0])
            print("Computer Wins!")


rock.main(rock.user())