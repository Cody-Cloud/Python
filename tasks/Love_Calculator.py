"""
Author: Cody Swindells
Created: 5/08/21
Modfied: 18/08/21
A 'love' calculator made for the purpose interactive coding exercise

It's main purpose is to determine whether by name, that a couple are compatible. 

#BUG Current - Expected value has not been achieved for the calculator -fixed 

Completed
"""
class Love:
    """
    Class: Love

    Functions: calculate, main, exit
    
    """
    Exit = ''
    def calculate (firstPerson, secondPerson):
        """
        Calculate capatibility based off 

        Parameters:
        
        firstPerson - First member of couple

        secondPerson - Second member of couple

        Returns:

        total score of capatible
        
        """
        true = "true"
        love = "love"
        total_true = 0
        total_love = 0
        total = 0

        for i in range(len(true)-1): #BUG - expected value has not been achieved
           total_true += firstPerson.count(true[i])
           total_love += secondPerson.count(true[i])
           print(str(i))
           print(true[i])
           print(total_true)
           print(total_love)
        for u in range(len(love)-1):
            total_true += firstPerson.count(love[u])
            total_love += secondPerson.count(love[u])
            print(total_true)
            print(total_love)
        total = int(str(total_true) + str(total_love))
        if total < 10 or total > 90:
            print("Your score is " + str(total) + ", you go together like coke and mentos.")
        elif total >= 40 and total <= 50:
            print("Your score is " + str(total) + ", you go together like coke and mentos.")
        else:
            print("Your score is " + str(total))
    def exit ():
        """
        Checks if the user wants to exit the program
        """
        exit = input("Would you like to exit? ").lower()
        if exit == "exit":
            return "exit"
        else:
            return 0
    def main ():
        """
        Main function loop
        """

        while(Love.Exit != 'exit'):#might be this part that is causing the bug - #Fixed It was the place of the function that was the problem.

            firstPerson = input("Please enter the name of the first person. " ).lower() #convert to lowercase - ensure that case doesn't become a factor
            secondPerson = input("Please enter the name of the second person. " ).lower()

            Love.calculate(firstPerson, secondPerson)
            Love.Exit = Love.exit()

if __name__ == "__main__":
    Love.main() #BUG! Goes straight to exit without actually doing anything - must fix  #BUG FIXED!