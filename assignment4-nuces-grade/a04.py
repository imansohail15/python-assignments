## IMPORTS GO HERE
# no imports are needed
## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(total_marks): # function to convert marks into grade
    total_marks = round(total_marks) # round marks to nearest integer
    if total_marks >=90:
        return 'A+'
    
    elif total_marks >=86:
        return "A"
    
    elif total_marks >=82:
        return "A-"
    
    elif total_marks >=78:
        return "B+"
    
    elif total_marks >= 74:
        return 'B'

    elif total_marks >= 70:
        return 'B-'

    elif total_marks >= 66:
        return 'C+'

    elif total_marks >= 62:
        return 'C'

    elif total_marks >= 58:
        return 'C-'

    elif total_marks >= 54:
        return 'D+'

    elif total_marks >= 50:
        return 'D'

    # Marks below 50 get grade F
    else:
        return 'F'
        
#### End OF MARKER

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
def calculate_sgpa(grade1, grade2, grade3): # function to calculate sgpa from 3 grades
    total_points = 0 # total grade points
    total_subjects = 0 # number of subjects counted
    grades = { # grade to point conversation table
        'A+': 4.00,
        'A': 4.00,
        'A-': 3.67,
        'B+': 3.33,
        'B': 3.00,
        'B-': 2.67,
        'C+': 2.33,
        'C': 2.00,
        'C-': 1.67,
        'D+': 1.33,
        'D': 1.00,
        'F': 0.00
    }
    if grade1 != 'nothing': # check first grade
        total_subjects +=1 # increase subject count
        total_points +=grades[grade1] # add grade point to total
        
    if grade2 != 'nothing': # check second grade
        total_subjects +=1 # increase subject count
        total_points += grades[grade2] # add grade point to total 
        
    if grade3 != 'nothing': # check third grade
        total_subjects +=1 # increase subject count
        total_points += grades[grade3] # add grade point to total 
        
    if total_subjects==0: # if no subject are provided
        return 0
    return total_points/total_subjects # calculate and return sgpa
#### End OF MARKER




if __name__ == '__main__':
    print (get_grade(98))
    print (calculate_sgpa('A', 'B', 'nothing'))