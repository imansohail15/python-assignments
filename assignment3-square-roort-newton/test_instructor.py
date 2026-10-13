try:                                                    # try to import the required function from a03.py
    from a03 import sqrt, average, improve_guess
except:                                                 # if import fails, do nothing
    pass
epsilon = 1e-4                                          # allowed errors when capturing decimal numbers

def test_avg_float():                                   # test average using decimal numbers
     a = 0.1112
     b = 0.1113
     assert abs(average(a, b)- 0.11125) < epsilon       # check if the average is correct 
     
def test_avg_int():                                     # test average using integers
        a = 1
        b = 2
        assert abs(average(a, b) - 1.5) < epsilon       # check if the average is correct

def test_avg_int_2():
    a = 35112
    b = 35113
    assert abs(average(a, b) - 35112.5) < epsilon       # check if the average is correct
    
def test_sqrt_int():                                    # test sqrt function
    v = 674
    assert abs(sqrt(v)- 25.961509) < epsilon            # check if the square root is correct
    
def test_improve_guess():                               # test improve_guess with a float guess
    n = 54                                              # original number
    g = 7.0                                             # current guess
    res = improve_guess(g , n)                          # get improved guess
    assert abs(res - 7.3571) < epsilon                  # check if the result is correct 
    
def test_improve_guess_zero():                          # test improve_guess when guess is zero
    n = 1e-7                                            # very small number
    g = 0                                               # initial guess
    res = improve_guess(g, n)                           # get improved guess
    assert abs(res - 5.000000005 ) < epsilon            # check if the result is correct
    
def test_improve_guess_2():                             # test improve guess using integer guess
    n = 54                                              # original number
    g = 7                                               # current guess
    res = improve_guess(g , n)                          # get improved guess
    assert abs(res - 7.3571) < epsilon                  # check if the result is correct
    
def test_improve_guess_2_dup():                         # duplicate test to give more weight to this case
    n = 54                                              # original number
    g = 7                                               # current guess
    res = improve_guess(g , n)                          # get improved guess
    assert abs(res - 7.3571) < epsilon                  # check if the result is correct
    
    
# output capturing decorator
def capture_output(fn):                                 # this function captures whatever the given function prints
    def wrapper(*args, **kwargs):                       # wrapper function that accept any arguments
        import StringIO                                 # StringIO is used to store printed text temporarily
        import sys                                      # sys is used to control python's standard output
        orig_stdout = sys.stdout                        # save the original output destination
        capturedOutput = StringIO.StringIO()            # create a temporary place to store output
        sys.stdout = capturedOutput                     # send print output to the capturedoutput instead of the screen
        v= fn(*args, **kwargs)                          # run the original function
                                                        # its return value is stored in v
        sys.stdout = orig_stdout                        # restore the normal output
        output_val = capturedOutput.getvalue()          # get the text that was printed by the function
        return v, output_val                            # return both the function result and captured output
    return wrapper                                      # return the wrapper function    