try:
    from a02 import get_area, output_parameter            # import get_area and output_parameter functions from a02.py 
except:
    pass                                                  # if import fails,do nothing

epsilon = 0.001                                           # allowed difference for floating point calculations

import math                                               # import python's math module
def test_floats():                                        # Test get_area() with different floating-point values
    vals = [ 2.0 , 2.9 , 1.9 , 22.0 , 3.09 ]              # different radius values to test
    for v in vals:                                        # take each radius value one by one
       assert abs(get_area(v) - (math.pi*v*v))<epsilon    # check that get_area() gives the correct area
                                                          # formula for circle area= pi*radius*radius
                                                          # abs() gets the positive difference
                                                          # difference should be less than epsilon
def test_parameter_float():                               # test parameter_output with a floating point radius
    val=1.999                                             # radius value for this test
    v, out = capture_output(output_parameter)(val)        # run output parameter() and capture its printed output
                                                          # v= function's return value 
                                                          # out= text printed by the function
    assert out.startswith("The parameter of the circle with radius 1.999 is 12.560")    #check that output starts with required message

#output capturing decorator
def capture_output(fn):                        # this function captures whatever the given function prints
    def wrapper(*args,**kwargs):               # wrapper function that accept any arguments
        import StringIO                        # stringIO is used to store printed text temporarily
        import sys                             # sys is used to control python's standard output
        orig_stdout=sys.stdout                 # save the original output destination
        capturedOutput=StringIO.StringIO()     # create a temporary place to store output
        sys.stdout=capturedOutput              # send print output to the capturedoutput instead of the screen
        v=fn(*args,**kwargs)                   # run the original function
                                               # its return value is stored in v
        sys.stdout=orig_stdout                 # restore the normal output
        output_val=capturedOutput.getvalue()   # get the text that was printed by the function
        return v,output_val                    # return both the function result and captured output
    return wrapper                             # return the wrapper function