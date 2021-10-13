"""

Author: Cody Swindells

Modfied: 06/10/21

"""

import exit

class leapYear:

    def Leap():
        """
        A function which determine if a year is a leap year.
        .ie on every year that is evenly divsible by 4 except every year
        that is evenly divisable by 100 unless the year is also
        divisible by 400
        Parameters:
            year - the year that will be checked
        """
        leapYearCK = int(input("Input the year to be checked.\n "))
        year = leapYearCK
        if (leapYearCK % 4 == 0 and leapYearCK % 100 > 0):
            print(str(year) + " is a leap year.")
        elif (leapYearCK % 100 == 0 and leapYearCK % 400 == 0):
            print(str(year) + " is a leap year.")
        else:
            print(str(year) + " is not a leap year.")
            
    def main():
        """
        """
        leapYear.Leap()

leapYear.main()

    
