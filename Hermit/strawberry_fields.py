#!/usr/bin/env checkio --domain=py run strawberry-fields

# Let's grow strawberries!
# 
# But . . . all kids in the neighborhood are fond of strawberries, so we need to protect our precious plants by placing a fence.
# 
# The fence is made of 4 parts (a, b, c, d) and each of them has (but not necessarily) a different length. They are going to be placed around the field in a counterclockwise order.
# 
# It's up to you to write a function that returns (in degrees) the angle of the inside corner α which forms between the first and last part of the fence (a and d) so that the fence encloses the maximum area for our strawberry bed.
# 
# You are given four numbers (a, b, c, d) that represent the lengths of the four fence parts. Your function has to return the angle measured from the inside and formed in order to enclose the maximum area. The angle we are searching for should be rounded to one tenth of a degree (fig.1).
# 
# 
# 
# Input:Four numbers.
# 
# Output :A number rounded to one decimal point.
# 
# 
# 
# 
# 
# Precondition:
# 
# ∀ length of all sides : length of one side <= sum length of three other sides
# 
# ∀ angle α of all corners : 0° <= α <= 180°
# 
# 
# END_DESC

def strawberryfield(a, b, c, d):

    # your code
    
    return 0


# These "asserts" are used for self-checking only and not for an auto-testing
if __name__ == '__main__':
    assert(strawberryfield(100, 100, 100, 100) == 90)  , "square"
    assert(strawberryfield(150, 100, 150, 100) == 90)  , "rectangle"   
    assert(strawberryfield(150, 100, 50, 100) == 60)   , "trapezium"
    assert(strawberryfield(203, 123, 82, 117) == 60.8) , "quadrilateral"
    
    print("Looks good so far! . . . How does 'Check' ?")