"""
Hangman project

Author: Cody Swindells

Created: 01/12/21

Modified: 04/12/21


"""
import random
import exit

class hangman:
    """
    Main object for hangman project
    
    """

    word_list = ["aardvark", "baboon", "camel"]

    chosen_word = ""

    blank_word = ""

    user_select = ""

    def select_word():
        """
        A function which selects a random word to be guess from a list.
        """
        computer_select = random.randint(0, len(hangman.word_list)-1)
        hangman.chosen_word = hangman.word_list[computer_select]

    def present_blank():
        """
        A function that present a certain number of blanks based on the word selected.
        
        """

        hangman.blank_word = '_'*len(hangman.chosen_word)
        print(hangman.blank_word)

    def ask_user():
        """
        Checks a user letter guess against a randomly word from a list.
        
        """
        guess = input(f"Please enter enter a letter. \n").lower()

        if(guess in hangman.chosen_word):
            print("Letter is in.")
        else:
            print("Letter is not in.")




    def main():
        """
        Main function exection for hangman project.
        
        """
        hangman.select_word()

        print(hangman.chosen_word)

        hangman.present_blank()
        hangman.ask_user()





exit.exitProgram.main(hangman.main) #import my exit function loop for now.