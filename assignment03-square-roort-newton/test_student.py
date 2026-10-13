try:                                                # try to import the required functions from a03.py
    from a03 import sqrt, improve_guess, average
except ImportError:                                 # if the file or functions are not found
    pass                                            # ignore the error and continue
epsilon = 1e-4                                      # allowed error when comparing decimal numbers

def test_avg_float():                               # test average using float numbers
    a = 1.0                                         # first float value
    b = 3.0                                         # second float value
    assert abs(average(a, b) - 2.0) < epsilon       # check if the average is correct
    
def test_avg_int():                                 # test average using integer numbers
    a = 1                                           # first integer value
    b = 2                                           # second integer value
    assert abs(average(a, b) - 1.5) < epsilon       # check if the average is correct
    
def test_sqrt_int():                                # test sqrt function with an integer
    v = 36                                          # integer value to find the square root of
    assert abs(sqrt(v) - 6) < epsilon               # check if the square root is correct
    
def test_improve_guess():                           # test improve_guess function
    n = 36                                          # original number
    g = 4                                           # current guess
    assert abs(improve_guess(g, n) - 6.5) < epsilon # check if the improved guess returns 6.5
    