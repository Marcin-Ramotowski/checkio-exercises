#!/usr/bin/env checkio --domain=py run cut-into-squares

# 
# 
# You are given a rectangle, which is defined by its widthwand heighth, both positive integers. We allow a rectangle to be cut into two smaller rectangles with either a straight horizontal or a straight vertical cut at any integer position. For example, one of the possible ways to cut the rectangle (5, 8) in two pieces would be to cut it into (2, 8) and (3, 8). Another way would be to cut it into two pieces is (5, 4) and (5, 4) etc. The resulting smaller pieces can then be further cut into smaller pieces, as long as the length of the side being cut is at least two to allow a cut. You are NOT allowed to cut multiple pieces in one motion of the blade by stacking pieces on top of each other.
# 
# Your task is to keep cutting the given rectangle into smaller pieces until each piece is a square, that is, the width of each piece equals its own height. This is always possible, since you could just keep cutting until the size of each piece has become 1-by-1. However, this function should return the smallest number of cuts that makes each piece a square.
# 
# Input:Two integers(int).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert cut_into_squares(4, 4) == 0
# assert cut_into_squares(4, 2) == 1
# assert cut_into_squares(7, 6) == 4
# 
# Feel yourself in need of a hint? Click on this line.This problem is best solved with recursion. Its base cases are when w==h for a piece that is already a square so you return 0, and when min(w,h)==1 allowing no further cuts on the shorter side, return max(w,h)-1.  Otherwise, loop  through  the  possible  ways  to  cut  this piece into two smaller pieces, recursively computing the best possible way to cut up these two pieces. Return the number of cuts produced by the optimal way of cutting this piece. Since this branching recursion would visit its  subproblems  exponentially  many  times,  you  will  surely  want  to  sprinkle  some@lru_cachememoization magic on it to downgrade that exponential tangle into a mere quadratic one.
# 
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def cut_into_squares(w: int, h: int) -> int:
    # your code here
    return 0


print("Example:")
print(cut_into_squares(3, 2))

# These "asserts" are used for self-checking
assert cut_into_squares(4, 4) == 0
assert cut_into_squares(4, 2) == 1
assert cut_into_squares(7, 6) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")