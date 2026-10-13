try:
     from a05 import is_prime , get_largest_prime, output_factors
except ImportError:
    pass # if the file not found ignore the error and continue

def test_isprime_1(): # check if prime check works correctly for multiple positive prime numbers
    for i in [5 , 139 , 631 , 919]:
        assert is_prime(i)==True
        
def test_isprime_float(): # test if another float with a non zero decimal part returns false for is_prime
    assert is_prime(6.0)== False
    
def test_isprime_float2(): # test if another float with a non zero decimal part correctly returns false
    assert is_prime(6.09)== False
    
def test_get_prime_1(): # test if get_largest_prime finds the correct largest prime<= 7920
    assert get_largest_prime(7920)==7919
    
def test_get_prime_2(): # test if get_largest_prime finds the correct largest prime<= 7920
    assert get_largest_prime(87)==83
    
def test_get_prime_3(): # test if get_largest_prime correctly handles float input like 87.9 by converting
    assert get_largest_prime(87.9)==83
    
def test_get_prime_4(): # test if get_largest_prime returns None when 0 is passed
    assert get_largest_prime(0)==None

def test_get_prime_5(): # test if get_largest_prime returns the number it self if it is already prime
    assert get_largest_prime(7)==7
    
def test_output_factors_1(): # test if output_factors correctly prints all factors of 10 line by line
    v,out = capture_output(output_factors)(10)
    assert out=='\n'.join([str(x) for x in [1,2,5,10]])+ "\n"
    
def test_output_factors_2():
    v,out=capture_output(output_factors)(99) # test if output_factors correctly prints all factors of 99 line by line
    assert out=='\n'.join([str(x) for x in [1,3,9,11,33,99]]) + "\n"
    
#output capturing decorator
def capture_output(fn):
    def wrapper(*args , **kwargs):
        import StringIO
        import sys
        orig_stdout=sys.stdout
        capturedoutput=StringIO.StringIO()
        sys.stdout=capturedoutput
        v=fn(*args,**kwargs)
        sys.stdout=orig_stdout
        output_val=capturedoutput.getvalue()
        return v,output_val
    return wrapper