"""

Author: Cody Swindells

Created: 05/10/21

Modfied: 05/10/21

Find the sum of numbers between 1 and 100

Restriction:

Can't use the sum function

Completed

"""

class evenSum:
    """
    Main class object
    """
    def main():
        """
        Main function the to find the sum of even number
        between one and one hundred.
        """
        sum = 0
        for i in range(1, 100):
            if(i % 2 == 0):
                sum += i
        print(f"The sum is {sum}")

evenSum.main()
