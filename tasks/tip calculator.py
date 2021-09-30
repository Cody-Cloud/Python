"""

Author: Cody Swindells

A previous code challange I had completed that calculats tips

"""

import unicodedata

class tips:
    def is_Number(string):
        try:
            int(string)
            return True
        except ValueError:
            pass
        try:
            unicodedata.numeric(string)
            return True
        except (TypeError, ValueError):
            pass
        return False

    def main():
        """
        Main program for the tip calculator

        Adds an extra exit option and infinite loop

        Build prior commence day 2 so I can skip day 2

        Author: Cody Swindells

        Current bug: Fixed


        """
        exit = ""

        while(exit != "exit"):

            print('Welcome to the tip calculator.\n')


            tip = 0

            total_bill = input("What was the total bill?\n")
            while(tips.is_Number(total_bill) == False): #attribute error to fix #Fixed
                print('Please enter a number.\n')
                total_bill = input("What was the total bill?\n")
            
            total_people = input("How many people to split the bill?\n")
            while(tips.is_Number(total_people) == False):
                print('Please enter a number.\n')
                total_people = input("How many people to split the bill?\n")

            percentage = input("What percentage tip would you like to give? 10 , 12, or 15? \n")
            while(tips.is_Number(percentage) == False):
                print('Please enter a number.\n')
                percentage = input("What percentage tip would you like to give? 10 , 12, or 15? \n")

            total_bill = int(total_bill)
            total_people = int(total_people)
            percentage = int(percentage)

            if (percentage == 10):
                tip = (total_bill * 0.1) / total_people
            elif (percentage == 12):
                tip = (total_bill * 0.12) / total_people
            elif (percentage == 15):
                tip = (total_bill * 0.15) / total_people
            else:
                print(total_bill)
                print(total_people)
                print(percentage)
                print("Eh, oh well\n")

            print("Each person should pay: \n" + " " + str(tip))

            exit = input("Do you want to exit? Type exit \n").lower()

tips.main()
