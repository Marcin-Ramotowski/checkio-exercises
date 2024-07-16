#!/usr/bin/env checkio --domain=py run maximum-among-three

# Given three integers, determine which one is the largest.
# 
# 
# 
# Input:Three integers(int).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert max_of_three(1, 2, 3) == 3
# assert max_of_three(3, 2, 1) == 3
# assert max_of_three(1, 3, 2) == 3
# assert max_of_three(0, 0, 0) == 0
# Precondition:-109<= a, b, c <= 109.
# 
# 
# END_DESC

def max_of_three(a: int, b: int, c: int) -> int:
    # your code here
    return 0


print("Example:")
print(max_of_three(1, 2, 3))

# These "asserts" are used for self-checking
assert max_of_three(1, 2, 3) == 3
assert max_of_three(3, 2, 1) == 3
assert max_of_three(1, 3, 2) == 3
assert max_of_three(0, 0, 0) == 0
assert max_of_three(-1, -2, -3) == -1
assert max_of_three(5, 5, 4) == 5
assert max_of_three(-5, -5, -6) == -5
assert max_of_three(10, 9, 10) == 10
assert max_of_three(123, 456, 789) == 789
assert max_of_three(789, 123, 456) == 789

print("The mission is done! Click 'Check Solution' to earn rewards!")