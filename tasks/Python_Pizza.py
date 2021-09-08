"""
Author: Cody Swindells

Created and Modified: 7/30/21

In response to a interactive problem in Udemy Python Course

Made use of classes
Nested if statements

"""
class cost:
    """
    Object encompass the main methods of calculating the pizza order
    """
    small = (15, 2, 1)
    medium = (20, 3, 1)
    large = (25, 3, 1)
    def calcOrder (size, add_pepperoni, extra_cheese):
        """
        Calculate the pizza order

        Parameters:

        Size - Size of the pizza

        add_pepperoni - does the user want to add pepperoni to the pizza

        extra_cheese - does the user want to extra cheese

        return:

        print of the order

        """
        i = 0
        total = 0

        if size == 'S':
            i = 0
            for i in range(len(cost.small)):
                if add_pepperoni == 'Y' and extra_cheese == 'Y':
                    total += cost.small[i]
                elif add_pepperoni == 'N' and extra_cheese == 'Y':
                    if extra_cheese == 'Y' and i != 1:
                        total += cost.small[i]
                elif add_pepperoni == 'Y' and extra_cheese == 'N':
                    if i < 2:
                        total += cost.small[i]
                elif extra_cheese == 'N' and i == 0:
                    total += cost.small[i]
        if size == 'M':
            i = 0
            for i in range(len(cost.medium)):
                if add_pepperoni == 'Y' and extra_cheese == 'Y':
                    total += cost.medium[i]
                elif add_pepperoni == 'N' and extra_cheese == 'Y':
                    if extra_cheese == 'Y' and i != 1:
                        total += cost.medium[i] 
                elif add_pepperoni == 'Y' and extra_cheese == 'N':
                    if i < 2:
                        total += cost.medium[i]
                elif extra_cheese == 'N' and i == 0:
                    total += cost.medium[i]
        if size == 'L' or size == 'XL':
            i = 0
            for i in range(len(cost.large)):
                if add_pepperoni == 'Y' and extra_cheese == 'Y':
                    total += cost.large[i]
                elif add_pepperoni == 'N' and extra_cheese == 'Y':
                    if extra_cheese == 'Y' and i != 1:
                        total += cost.large[i] 
                elif add_pepperoni == 'Y' and extra_cheese == 'N':
                    if i < 2:
                        total += cost.large[i]
                elif extra_cheese == 'N' and i == 0:
                    total += cost.large[i]              
        return total
    def welcomeOrder ():
        """
        Prompts the user to make an order and prints the resulting bill
        """
        print("Welcome to Python Pizza Deliveries!")
        size = input("What size pizza do you want? S, M, L, XL ").upper()
        add_pepperoni = input("Do you want pepperoni? ").upper()
        extra_cheese = input("Do want Extra cheese ").upper()

        print('Your pizza order total is $ ' + str(cost.calcOrder(size, add_pepperoni, extra_cheese)))
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
        Main program 
        """
        exit = ""

        while exit != 'exit':
            cost.welcomeOrder()

            exit = cost.exit()

cost.main()        