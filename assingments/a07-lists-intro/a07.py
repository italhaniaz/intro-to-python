## IMPORTS GO HERE

## END OF IMPORTS
def valid_grade(grade_list):
    possible_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']

    for i in grade_list:
        found = False
        
        for j in possible_grades:
            if i == j:
                found =  True
                break
    
        if found == False:
            return False
    
    return True
#####################
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
#######################

### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###
def calculate_sgpa(grade_list):
    if grade_list == None:
        return None
    
    if isinstance(grade_list, str):
        grade_list = [grade_list]
   
    if not valid_grade(grade_list):
        return None
    
    total_marks = 0
    total_number_of_subjects = 0

    for i in grade_list:
        if i != 'nothing':
            total_number_of_subjects = total_number_of_subjects + 1
            total_marks = total_marks + get_points(i)

    if total_number_of_subjects == 0:
        return 0

    sgpa = total_marks / total_number_of_subjects
    return sgpa
#### End OF MARKER

### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted(grade_lst, credit_hrs_lst):
    if grade_lst == None or credit_hrs_lst == None:
        return None
    if isinstance(grade_lst, str):
        grade_lst = [grade_lst]
    if isinstance(credit_hrs_lst, int):
        credit_hrs_lst = [credit_hrs_lst]
    if not valid_grade(grade_lst):
        return None
    if len(grade_lst) != len(credit_hrs_lst):
        return None
    
    total_credits = 0
    
    for grade, credit_hours in zip(grade_lst, credit_hrs_lst):
        grade_points = get_points(grade)
        total_credits = total_credits + (grade_points * credit_hours)
    
    weight_sum = 0
    weight_sum = sum(credit_hrs_lst)

    if weight_sum == 0:
        return None
    
    sgpa = total_credits / weight_sum

    return sgpa
#### End OF MARKER


if __name__ == '__main__':
    print (calculate_sgpa(["A+", "B", "B+"]))
    print (calculate_sgpa_weighted('D+', 4))
