"""

Author: Cody Swindells

Creation Date: 07/19/21

Updated: 04/08/21 

Hopetheical Ticket system for a hypotheical carnvial ride.

"""
class TicketRide:
    def Ride (height, age):
        """
        test to see whether and individual is able to ride

        Parameters:

        height -  the height of the individual

        age - the age of the individual
        

        """
        cost = 0
        canRide = False

        if height > 120:
            if age < 12:
                cost = 5
                canRide = True
                return (cost, canRide)
            elif (age >= 12 and age <= 18):
                cost =  7
                canRide = True
                return (cost, canRide)
            elif age > 18:
                cost = 12
                canRide = True
                return (cost, canRide)
        else:
            return (cost, canRide)
                    
    def plusPhoto ():
        """
        Returns a boolean value based on whether user wants photos or not

        """
        wantPhoto = input("Do you want photos? ").lower()

        if wantPhoto == "yes":
            return True
        else:
            return False

    def ticketCost (cost, total):
        '''
        To print ticket and total bill cost to the console

        Parameters:
        cost - Ticket Cost

        total - Total bill 
        '''
        print("Your ticket cost will be $" + str(cost))
        print("Your total cost will be $" + str(total))

    def totalBill(cost, canRide, photo):
        """
        Determines the total cost to the ride

        Parameters:

        cost - ticket cost based of age and height

        canRide - the minimum requirement to be allowed to ride

        photo - whether the user wants to buy photos
        """
        total = 0
        costTicket = cost

        if photo == True and canRide == True:
            total = costTicket + 3
            TicketRide.ticketCost(costTicket, total)
        elif photo == False and canRide == True:
            total = costTicket
            TicketRide.ticketCost(costTicket, total)
        else:
            print("You can't ride.")

    def main ():
        """
        Main program function
        """
        while(1):

            userHeight = int(input("What is your height in cm? "))
            userAge = int(input("What is your age? "))
            
            photo = TicketRide.plusPhoto()
            

            TicketRide.totalBill(TicketRide.Ride(userHeight, userAge)[0], TicketRide.Ride(userHeight, userAge)[1], photo)

TicketRide.main()

