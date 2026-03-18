## IMPORTS GO HERE
import math
## END OF IMPORTS

def get_rounded_marks(marks):
    x = math.floor(marks)
    x = marks - x

    if x == 0:
        return marks
    elif x < 0.5:
        return math.floor(marks)
    else:
        return math.ceil(marks)


#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(total_marks):

    if total_marks <= 0 or total_marks > 100:
        return None
    
    total_marks = get_rounded_marks(total_marks)

    if total_marks >= 90:
        return "A+"
    elif total_marks >= 86:
        return "A"
    elif total_marks >= 82:
        return "A-"
    elif total_marks >= 78:
        return "B+"
    elif total_marks >= 74:
        return "B"
    elif total_marks >= 70:
        return "B-"
    elif total_marks >= 66:
        return "C+"
    elif total_marks >= 62:
        return "C"
    elif total_marks >= 58:
        return "C-"
    elif total_marks >= 54:
        return "D+"
    elif total_marks >= 50:
        return "D"
    else:
        return "F"

#### End OF MARKER

def get_points(grade):

    if grade == "A+" or grade == "A":
        return 4.00
    elif grade == "A-":
        return 3.67
    elif grade == "B+":
        return 3.33
    elif grade == "B": 
        return 3.00
    elif grade == "B-":
        return 2.67
    elif grade == "C+":
        return 2.33
    elif grade == "C": 
        return 2.00
    elif grade == "C-":
        return 1.67
    elif grade == "D+":
        return 1.33
    elif grade == "D": 
        return 1.00
    else:
        return 0.00    
#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
def calculate_sgpa(grade1, grade2, grade3):
    total_marks = 0
    total_num_of_subjects = 0

    if grade1 != "nothing":
        total_num_of_subjects = total_num_of_subjects + 1
        total_marks = get_points(grade1) + total_marks
    
    if grade2 != "nothing":
        total_num_of_subjects = total_num_of_subjects + 1
        total_marks = get_points(grade2) + total_marks

    if grade3 != "nothing":
        total_num_of_subjects = total_num_of_subjects + 1
        total_marks = get_points(grade3) + total_marks
    
    if total_num_of_subjects == 0:
        return 0
    
    sgpa = total_marks / total_num_of_subjects
    return sgpa
#### End OF MARKER




if __name__ == '__main__':
    print (get_grade(50))
    print (calculate_sgpa('A', 'B', 'nothing'))
