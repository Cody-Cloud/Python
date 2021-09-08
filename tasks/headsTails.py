"""
Author: Cody Swindells

Created: 23/08/21

"""

import random

class headsTails:

    exit = ""

    def calcFlip():
        coin = random.random()

        if(coin < 0.5):
            print("The coin flip reveals Tails")
        else:
            print("The coin flip reveals Heads")
    def main():
        while(headsTails.exit != "exit"):
            headsTails.calcFlip()
            headsTails.exit = input("Do you want to exit?").lower()

headsTails.main()