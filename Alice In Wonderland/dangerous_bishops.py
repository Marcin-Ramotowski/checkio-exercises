#!/usr/bin/env checkio --domain=py run dangerous-bishops

# The generalized square chessboard has been taken over by an army ofbishops, each bishop represented as a two-tuple(row, col)(0-base indexing) of the coordinates of the square that the bishop stands on. Given the board sizenand the list of bishops on that board, count the number of safe squares that are not covered by any bishop.
# 
# Let's look at the case4, [(2, 3), (0, 1)], which is11.
# 
# 
# 
# Click this line if you need a hintTo check whether two squares (r1, c1) and (r2, c2) are reachable from each other in a single bishop move, the expression abs(r1-r2)==abs(c1-c2) checks that the horizontal distance between those squares equals their vertical distance, which is both necessary and sufficient for those squares  to lie on  the same diagonal. This way you don’t have  to separately rewrite  the essentially identical block of logic four times, but one test handles all four diagonal directions in one swoop.
# 
# Input:Two arguments. Integer(int)andlistof tuples of two integers.
# 
# Output:Integer.
# 
# Examples:
# 
# assert safe_squares(10, []) == 100
# assert safe_squares(4, [(2, 3), (0, 1)]) == 11
# assert safe_squares(8, [(1, 1), (3, 5), (7, 0), (7, 6)]) == 29
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def safe_squares(n: int, bishops: list[tuple[int, int]]) -> int:
    # your code here
    return 0


print("Example:")
print(safe_squares(10, []))

# These "asserts" are used for self-checking
assert safe_squares(10, []) == 100
assert safe_squares(4, [(2, 3), (0, 1)]) == 11
assert safe_squares(8, [(1, 1), (3, 5), (7, 0), (7, 6)]) == 29

print("The mission is done! Click 'Check Solution' to earn rewards!")