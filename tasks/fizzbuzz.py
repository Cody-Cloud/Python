"""
Author: Cody Swindells

Created: 06/10/21

Modfied: 06/10/21

Completed
"""

class fizzBuzz:
    """
    Main class object
    """
    def main():
        """
        Main function that prints a number or Fizz if divisable 3
        or Buzz if divisable by 5 or FizzBuzz if divisable by 3 and 5. 
        """
        for i in range(1, 101): # range is between so 1 - 101 has be to get 100 to print
            if(i % 3 == 0 and i % 5 == 0):
                print("FizzBuzz")
            elif(i % 3 == 0):
                print("Fizz")
            elif(i % 5 == 0):
                print("Buzz")
            else:
                print(i)

fizzBuzz.main()