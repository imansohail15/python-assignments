def get_grade_point(grade):
    mapping={
        'A+':4.0 , 'A':4.0,
        'A-':3.67 ,
        'B+':3.33 , 'B':3.0,
        'B-':2.67 ,
        'C+':2.33 , 'C':2.0,
        'C-':1.67 ,
        'D+':1.33 , 'D':1.0,
        'F':0.0
        }
    if grade in mapping:
        return mapping[grade]
    return None
def calculate_sgpa(grades):
    if grades is None:
        return None
    if isinstance(grades,str):
        grades=[grades]
    if len(grades)==0:
        return 0.0
    total_points=0.0
    count=len(grades)
    for g in grades:
        gp=get_grade_point(g)
        if gp is None:
            return None
        total_points +=gp
    return total_points/count

def calculate_sgpa_weighted(grades,weights):
    if grades is None or weights is None:
        return None
    if isinstance(grades,str):
        grades=[grades]
    if isinstance(weights,(int,float)):
        weights=[weights]
    if len(grades) !=len(weights):
        return None
    if len(grades)==0:
        return 0.0
    weighted_sum=0.0
    total_weights=0.0
    for g,w in zip(grades,weights):
        gp=get_grade_point(g)
        if gp is None or w is None or w<0:
            return None
        weighted_sum +=gp*w
        total_weights +=w
        if total_weights==0:
            return 0.0
        return weighted_sum/total_weights


if __name__=='__main__':
    print (calculate_sgpa(['A+']))
    print(calculate_sgpa_weighted(['A+'],[4]))