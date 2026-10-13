try:
    from a04 import get_grade, calculate_sgpa  
except:
    pass
epsilon = 1e-3 

def test_grade_float_1():
    score = 89.50
    assert get_grade(score) == 'A+'
    
def test_grade_float_2():
    score = 89.49
    assert get_grade(score) == 'A'
    
def test_grade_float_3():
    score = 89.1
    assert get_grade(score) == 'A'
    
def test_grade_float_4():
    score = 49.49
    assert get_grade(score) == 'F'
    
# Test SGPA when only grade F is provided
def test_sgpa_int_1():

    # SGPA should be 0
    assert abs(calculate_sgpa('nothing', 'F', 'nothing') - 0) < epsilon


# Test SGPA when only grade A is provided
def test_sgpa_int_2():

    # SGPA should be 4.0
    assert abs(calculate_sgpa('nothing', 'A', 'nothing') - 4.0) < epsilon


# Test SGPA with grades B+ and A
def test_sgpa_int_3():

    # (3.33 + 4.00) / 2 = 3.665
    assert abs(calculate_sgpa('nothing', 'B+', 'A') - 3.665) < epsilon


# Test SGPA with grades C- and B+
def test_sgpa_int_4():

    # (1.67 + 3.33) / 2 = 2.5
    assert abs(calculate_sgpa('C-', 'B+', 'nothing') - 2.5) < epsilon


# Test SGPA with grades C- and D+
def test_sgpa_int_5():

    # (1.67 + 1.33) / 2 = 1.5
    assert abs(calculate_sgpa('C-', 'D+', 'nothing') - 1.5) < epsilon


# Test SGPA when no subjects are provided
def test_sgpa_int_6():

    # Expected SGPA is 0
    assert abs(calculate_sgpa('nothing', 'nothing', 'nothing') - 0) < epsilon


# Test SGPA with grades D+ and B+
def test_sgpa_int_7():

    # (1.33 + 3.33) / 2 = 2.33
    assert abs(calculate_sgpa('D+', 'nothing', 'B+') - 2.33) < epsilon


# Test SGPA with grades C- and B+
def test_sgpa_int_8():

    # (1.67 + 3.33) / 2 = 2.5
    assert abs(calculate_sgpa('C-', 'nothing', 'B+') - 2.5) < epsilon
    
# output capturing decorator
def capture_output(func):
    import io
    import sys
    def wrapper(*args, **kwargs):
        # Capture the output of the function
        captured_output = io.StringIO()
        sys.stdout = captured_output
        func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()
    return wrapper
