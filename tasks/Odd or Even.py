while(1):
    number = int(input("What is the number to you want to check? "))
    storeNumber = number / 2


    if number % 2 > 0 :
      print(str(number) + " is odd because" + " " + str(number) + " ÷ 2 = " + str(storeNumber))
    elif number % 2 == 0:
      print(str(number) + " is even because" + " " + str(number) + " ÷ 2 = " + str(storeNumber))
