#!/usr/bin/env checkio --domain=py run rectangle-perimeter

# This function should take two positive numbers (length and width) as inputs and return the perimeter of a rectangle.
# 
# 
# 
# Input:Two integers(int).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert rectangle_perimeter(2, 4) == 12
# assert rectangle_perimeter(3, 5) == 16
# assert rectangle_perimeter(10, 20) == 60
# assert rectangle_perimeter(7, 2) == 18
# Preconditions:length, width ∈ R;length, width > 0.
# 
# 
# END_DESC

def rectangle_perimeter(length: int, width: int) -> int:
    # your code here
    return 0


print("Example:")
print(rectangle_perimeter(3, 2))

# These "asserts" are used for self-checking
assert rectangle_perimeter(2, 4) == 12
assert rectangle_perimeter(3, 5) == 16
assert rectangle_perimeter(10, 20) == 60
assert rectangle_perimeter(7, 2) == 18
assert rectangle_perimeter(1, 1) == 4
assert rectangle_perimeter(1, 5) == 12
assert rectangle_perimeter(4, 1) == 10
assert rectangle_perimeter(100, 100) == 400
assert rectangle_perimeter(0.5, 2) == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")