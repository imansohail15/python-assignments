def output_prime_factors(n):
    if isinstance (n,float):
        n=round(n)
    n=int(n)
    if n<=1:
        return
    d=2
    while d*d<=n:
        while n%d==0:
            print(d)
            n//=d
        d+=1
    if n>1:
        print(n)
def get_nth_prime(n):
    if isinstance(n,float):
        return None
    if n<1:
        return None
    count=0
    num=2
    while True:
        is_prime=True 
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
         count +=1
         if count==n:
            return num
         num +=1
    

if __name__ == '__main__':
    output_prime_factors(23)
    print (get_nth_prime(4))

                