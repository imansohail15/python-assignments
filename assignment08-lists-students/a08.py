## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(results):
    if results is None:
        return None
    if len(results)==0:
        return[]
    cumulative_results=[]
    
    for student in results:
        roll_no = student[0]
        name = student[1]
        scores = student[2:]
        total_marks=0.0
        
    for score in scores:
        if score is None:
            total_marks +=0.0
        else:
            total_marks +=float(score)
        cumulative_results.append((roll_no,name,total_marks))
    return cumulative_results
#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(results):
    if results is None:
        return None
    if len(results)==0:
        return None
    cum_marks_list= find_cumulative_marks(results)
    if not cum_marks_list:
        return None
    max_marks=-1.0
    for student in cum_marks_list:
        marks=student[2]
        if marks>max_marks:
            max_marks=marks
            top_students=[]
            for student in cum_marks_list:
                if student[2]==max_marks:
                    top_students.append((student[0],student[1]))
                if len(top_students)==1:
                    return top_students[0]
                else:
                    return top_students
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
