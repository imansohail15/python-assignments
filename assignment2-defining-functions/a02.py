## IMPORTS GO HERE
import math
## END OF IMPORTS 


#### YOUR CODE FOR get_area GOES HERE ####
def get_area(radius):
    return math.pi*radius*radius
#### End OF MARKER


#### YOUR CODE FOR output_parameter GOES HERE ####
def output_parameter(radius):
    parameter = 2*math.pi*radius
    print(f"The parameter of the circle with {radius} is {parameter}")
#### End OF MARKER  




if __name__ == '__main__': 
    print (get_area(2)) 
    output_parameter(1.0) 
