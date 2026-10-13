def is_prime(num):
    if type(num) not in (int,float):
        return False
    if num!=int(num):
        return False
    num=int(num)
    if num<=1:
        return False
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i +=1
        return True

def output_factors(num):
    if(type(num) not in (int,float) or num!=int(num)):
        return
    num=int(num)
    if num<=0:
        return
    i=1
    while i<=num:
        if num%i==0:
            print(i)
        i +=1
        
def get_largest_prime(num):
    if type(num) not in(int,float):
        return None
    num=int(num)
    current=num
    while current>=2:
        if is_prime(current):
            return current
        current -=1
        return None
    
# if __name__ == "__main__":
#     print("___Testing is_prime___")
#     print(is_prime(5.0))
#     print(is_prime(6.01))
#     print(is_prime(7))
    
#     print("\n __Testinf output_factors(for 10)___")
#     output_factors(10)
    
#     print("\n __Testing get_largest_prime___")
#     print(get_largest_prime(10))
#     print(get_largest_prime(1))
if __name__ == '__main__':
    print (is_prime(499))  # should return True

    print (get_largest_prime(10))  # should return 7
    # print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
