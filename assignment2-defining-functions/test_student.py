# try to import the required function from a02.py
try:
    from a02 import get_area, output_parameter
    
# if the file or function are not found, ignore the error
except ImportError:
    pass

# Allowed difference when comparing decimal values
epsilon = 0.001

# test get_area() using float value
def test_float():
    r=2.0                                          # radius of the circle
    result=12.566                                  # expected area value
    assert abs(get_area(r) - result) < epsilon     # check if calculated area is close to expected area
    
# test output_parameter with a float value
def test_parameter_float():
    val=0.1                                        #radius value 
    v, out = capture_output(output_parameter)(val) # run function and capture its printed output
    assert out.startwith("The parameter of the circle with radius 1.0 is 6.28") #check that output starts with required message

    
# Function decorator to capture printed output
def capture_output(fn):
    def wrapper(*args, **kwargs):                  # wrapper function that accept any arguments
        import StringIO                            # stringIO is used to store printed text automatically
        import sys                                 # sys is used to control python's standard output
        orig_stdout= sys.stdout                    # save the original output destination
        capturedOutput = StringIO.StringIO()       # create a temporary place to store output
        sys.stdout = capturedOutput                # send print output to the captureoutput instead of the screen
        v=fn(*args,**kwargs)                       # run the original function
                                                   # its run value is stored in v
        sys.stdout = orig_stdout                   # restore the normal output
        output_val = capturedOutput.getvalue()     # get the text that was printed by function 
        return v, output_val                       # return both the function result and captured output
    return wrapper                                 # return the wrapper function