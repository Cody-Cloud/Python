def Leap(year):
    """
    A function which determine if a year is a leap year.
        .ie on every year that is evenly divsible by 4 except every year
        that is evenly divisable by 100 unless the year is also
        divisible by 400
    Parameters:
        year - the year that will be checked
    """

    leapYear = year
    if leapYear % 4 == 0 and leapYear % 100 > 0:
        print(str(year) + " is a leap year.")
    elif leapYear % 100 == 0 and leapYear % 400 == 0:
        print(str(year) + " is a leap year.")
    else:
        print(str(year) + " is not a leap year.")
        
while(1):
    year = int(input("Enter a year to be checked. "))

    Leap(year)
 
