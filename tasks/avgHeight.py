"""
Author: Cody Swindells

Created: 05/10/21

Modfied: 05/10/21

Interactive coding task related to for loops

Example test data student_heights 156 178 165 171 187

Expected output:

171 as rounded to nearest whole number

Restrictions:

Can't use sum() or len() to each a solution

Completed


"""

class avgStarter:
    """
    Based code rework to fit the object oritentated programming style.

    Returns:

    student heights an array of user input 

    """

    def question():
        student_heights = input("Input a list of student heights \n").split()
        for n in range(0, len(student_heights)):
            student_heights[n] = int(student_heights[n])
        return student_heights

class avgMain:
    """
    Main class for calculating avg height data set
    """
    def main(user_input):
        """
        Main function for calculating avg height data set

        Parameters:

        An array based of avgStarter.question function or an array containing intergers.

        """
        avg_height = 0
        for i, item in enumerate(user_input): #loops through while also storing the index of each element
            avg_height += item
        avg_height = avg_height / (i + 1) # + 1 so that relects the total number as index starts with 0
        print(f"{round(avg_height)}\n") #round to down whole numbers

avgMain.main(avgStarter.question())
