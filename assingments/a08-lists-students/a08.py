## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(stu_records_lst):
    if stu_records_lst == None:
        return None
    if stu_records_lst == []:
        return []
    
    records_with_cumulative_marks = []
    cumulative_marks = []
    for i in stu_records_lst:
        total_marks = 0

        for j in i[2:]:
            if j != None:
                total_marks = total_marks + j

        cumulative_marks.append(total_marks)

    for i in range(0, len(stu_records_lst)):

        records_with_cumulative_marks.append((stu_records_lst[i][0], stu_records_lst[i][1], cumulative_marks[i]))
    
    return records_with_cumulative_marks
        
#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(stu_records_lst):
    cumulative_records = find_cumulative_marks(stu_records_lst)

    max_marks = 0
    max_mark_stu_index = 0

    for i in range(0, len(cumulative_records)):
        if max_marks < cumulative_records[i][2]:
            max_marks = cumulative_records[i][2]
            max_mark_stu_index = i
    
    top_sudent = (cumulative_records[max_mark_stu_index][0], cumulative_records[max_mark_stu_index][1])

    top_students_lst = [top_sudent]

    for i in range(max_mark_stu_index + 1, len(cumulative_records)):
        if max_marks == cumulative_records[i][2]:
            top_students_lst.append((cumulative_records[i][0], cumulative_records[i][1]))

    if len(top_students_lst) > 1:
        return top_students_lst
    else:    
        return top_sudent

#### End OF MARKER





if __name__ == '__main__':
    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]

    print (find_cumulative_marks(results))
    # output: [('p101111', 'Ali Khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6)]

    print (find_top_student(results))
    # output: ('p101111', 'Ali Khayam')
