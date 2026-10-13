try:
    from a06 import get_nth_prime,output_prime_factors
except ImportError:
    pass

def test_output_prime_factors_1():
    v,out = capture_output(output_prime_factors)(23)
    assert out =="\n".join([str(x) for x in [23]])+"\n"
    
def test_output_prime_factors_2():
    v,out = capture_output(output_prime_factors)(230)
    assert out =="\n".join([str(x) for x in [2,5,23]])+"\n"
    
def test_output_prime_factors_3():
    v,out = capture_output(output_prime_factors)(230.6)
    assert out =="\n".join([str(x) for x in [3,7,11]])+"\n"
    
def test_get_nth_prime_1():
    out=get_nth_prime(2)
    assert out==3
    
def test_get_nth_prime_2():
    out=get_nth_prime(2.1)
    assert out==None
    
def test_get_nth_prime_3():
    out=get_nth_prime(29)
    assert out==109
    
def capture_output(fn):
    def wrapper(*args,**kwargs):
        import StringIO
        import sys
        orig_stdout=sys.stdout
        capturedOutput=StringIO.StringIO()
        sys.stdout=capture_output
        v=fn(*args,**kwargs)
        sys.stdout=orig_stdout
        output_val=capture_output.getvalue()
        return v, output_val
    return wrapper
