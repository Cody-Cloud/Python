"""

Author: Cody Swindells

Modfied: 06/10/21

A previous task I completed way back.

"""

class BMI:

  """

  Main class object

  """

  def BMICAL (height, weight):
    """
    Determines BMI (Body Mass Index) based on weight and height

    Parameters: 
      height
      weight

    """
    BMI = weight / height ** 2

    if BMI < 18.5:
      print("You are under 18.5 BMI and are underweight.")
    elif BMI < 25:
      print("You are under 25 BMI and are slighty underweight.")
    elif BMI > 25 & BMI< 30:
      print("You are over 25 BMI but below 40, therefore are slighty overweight.")
    elif BMI > 30 & BMI < 35:
      print("You are over 30 but below 35 BMI, therefore are obese.")
    elif BMI > 35:
      print("You are over 35, therefore are clinically obese.")

  def main():
    """

    Main function

    """
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in m: "))
    BMI.BMICAL(height, weight)


BMI.main()