"""
Hangman project

Author: Cody Swindells

Created: 01/12/21

Modified: 13/12/21

Next stage: presenting hangman ascii art and progress til game is lost or won

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

    guess = ""

    string_arr = []

    letter_count = 0

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
        hangman.guess = input(f"Please enter enter a letter. \n").lower()

        if(hangman.guess in hangman.chosen_word):
            print("Letter is in.")
        else:
            print("Letter is not in.")
    def remain_blank():
        """
        A function that contine 

        """
        if(hangman.guess == ""):
            print("No guess made yet.")
        else:
            #hangman.string_arr.insert(hangman.chosen_word.index())

            if(hangman.chosen_word.count(hangman.guess, 0 + hangman.letter_count, len(hangman.chosen_word) - 1) != 0):
                #hangman.string_arr.insert(hangman.guess, hangman.chosen_word.find(hangman.guess) + 1)
                hangman.string_arr[hangman.chosen_word.find(hangman.guess,  0 + hangman.letter_count, len(hangman.chosen_word) - 1)] = hangman.guess
                hangman.letter_count += 1
                hangman.remain_blank()
            else:
                print(''.join(hangman.string_arr)) #by using ''.join it simplys the conversion back to a string.
            
    def initalise_game ():
        """
        A function that control main initilsation of the game.

        """
        hangman.select_word()

        print(hangman.chosen_word)

        hangman.present_blank()

        hangman.string_arr = list(hangman.blank_word)

    def main():
        """
        Main function exection for hangman project.
        
        """


        #will require a loop later with current computer selection and game instance

        hangman.initalise_game()
        hangman.ask_user()
        hangman.remain_blank()

    def clear_game():
        """
        A function that reset all variables for reinitaiisation
        
        """





exit.exitProgram.main(hangman.main) #import my exit function loop for now.