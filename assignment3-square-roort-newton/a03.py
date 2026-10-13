## IMPORTS GO HERE
# No import are neended for this assignment
## END OF IMPORTS


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(x):                            # function to calculate the square of the number
    if x==0:                            # if the number is 0 , return 0
        return 0
    guess = x/2                         # make an initial guess
    for i in range(20):                 # improve the guess 20 times
        guess = improve_guess(x, guess) # replace the old guess with a better guess
    return guess                        # return the final square root approximate
#### End OF MARKER


#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(a, b):                      # function to calculate the average of two numbers
    return(a + b) / 2                   # add both numbers and divide by 2
#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(x, a):                # function to generate a better square root guess
    return average(a, x/a)              # return the average of the current guess
#### End OF MARKER




if __name__ == '__main__':
    print (sqrt(36))