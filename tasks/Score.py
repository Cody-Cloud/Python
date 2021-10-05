"""
Author: Cody Swindells

Created: 05/10/21

Modfied: 05/10/21

Example test data:

78 65 89 86 55 91 64 89

Restrictions:

must not used min and max functions

Completed

"""

class scoreStarter:
    """
    Modfied based cose to fit object oritentated programming style.
    """
    def score_Data():
        """
        
        """
        student_scores = input("Input a list of student scores \n").split()
        for n in range(0, len(student_scores)):
            student_scores[n] = int(student_scores[n])
        print(student_scores)
        return(student_scores)

class Score:
    """
    """
    def main(user_input):
        """
        """
        maxi = user_input[0]
        mini = user_input[0]
        for item in user_input:
            if(item > maxi):
                maxi = item
            elif(item < mini):
                mini = item
        print(f"The Highest Score is {maxi} and lowest is {mini}\n")

Score.main(scoreStarter.score_Data())