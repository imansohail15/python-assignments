## IMPORTS GO HERE

## END OF IMPORTS


## START OF get_diag_sum FUNCTION
def get_diag_sum(n):
    if not isinstance(n,int) or isinstance(n,bool):
        return None
    if n<1 or n%2==0:
        return None
    if n==1:
        return 1
    current_sum=1
    current_val=1
    for current_n in range(3,n+1,2):
        step=current_n-1
        for _ in range(4):
            current_val +=step
            current_sum +=current_val
    return current_sum
        
## END OF MARKER



if __name__ == '__main__':
    print (get_diag_sum(5))
