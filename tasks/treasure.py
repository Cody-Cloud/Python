"""

Author: Cody Swindells

Created: 21/08/21

Modifed: 

Treasure Project 

"""
class treasure:
    checkGame = ""

    def printStart():
        """
        Print Tresaure chest ASCII art
        """
        print('''
        *******************************************************************************
                |                   |                  |                     |
        _________|________________.=""_;=.______________|_____________________|_______
        |                   |  ,-"_,=""     `"=.|                  |
        |___________________|__"=._o`"-._        `"=.______________|___________________
                |                `"=._o`"=._      _`"=._                     |
        _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
        |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
        |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
        _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
        |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
        |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
        ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
        /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
        ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
        /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
        ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
        /______/______/______/______/______/______/______/______/______/______/_____ /
        *******************************************************************************
        ''')


    def checkOver():
        treasure.checkGame = "over"

    def choices():
        leftRight = input("""
        You reach the beginning of journey and presented split in the road ahead. 
        Which way do you choose? Left or Right """).lower()
        if leftRight == "left":
            swimWait = input("""Your chosen path leads you to the docks. You now have two choices,
             you either wait and take the rickety dingy approaching in the distance or swim to the island. 
             Which choice will you make? """).lower()
            if swimWait == "wait":
                door = input("""The dingy arrives and you're able to get on board. 
                As you arrive on the Island and presented with three door; 
                guarding the only way to grand reward are three doors, blue, yellow and red.
                Which door will you choose? """)
                if door == "yellow":
                    print("""
                    Congratulation matey!!!!!!!!!!!!!! 
                    
               ,'``.._   ,'``.
              :,--._:)\,:,._,.:       All Glory to
              :`--,''   :`...';\      the HYPNO TOAD!
               `,'       `---'  `.
               /                 :
              /                   '"
            ,'                     :\.___,-.
           `...,---'``````-..._    |:       
             (                 )   ;:    )   \  _,-.
              `.              (   //          `'    
               :               `.//  )      )     , ;
             ,-|`.            _,'/       )    ) ,' ,'
            (  :`.`-..____..=:.-':     .     _,' ,'
             `,'\ ``--....-)='    `._,  \  ,') _ '``._
          _.-/ _ `.       (_)      /     )' ; / \ \`-.'
         `--(   `-:`.     `' ___..'  _,-'   |/   `.)
             `-. `.`.``-----``--,  .'
               |/`.\`'        ,','); SSt
                   `         (/  (/ """)
                elif door == "blue":
                    print("Beast descend upon you; eating you alive!!! GAME OVER!!")
                    treasure.checkOver()
                elif door == "red":
                    print("""You enter a dark room but as you enter the door slams behind you,
                    fire consumes you!!! GAME OVER!!!""")
                    treasure.checkOver()
            elif swimWait == "swim":
                print("A giant ass trout comes forth shallows you whole!! GAME OVER!!!")
                treasure.checkOver()     
        else:
            print("Walking along the path you fall into a hole!! GAME OVER!!")
            treasure.checkOver()

    def main():

        """
        Main program function the treasure project
        """

        print("Welcome to Treasure Island.\n")
        print("Your mission is to find the treasure.\n")

        while(treasure.checkGame != "over"):
            treasure.choices()
            

treasure.main()