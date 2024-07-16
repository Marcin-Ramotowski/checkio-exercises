#!/usr/bin/env checkio --domain=py run find-remainder

# Determine the remainder from division of two positive integers.
# 
# 
# 
# Input:Two integers(int): dividend (the number to be divided) and divisor (the number by which division is to be performed).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert find_remainder(10, 3) == 1
# assert find_remainder(14, 4) == 2
# assert find_remainder(27, 4) == 3
# assert find_remainder(10, 5) == 0
# Precondition:dividend, divisor > 0.
# 
# 
# END_DESC

def find_remainder(dividend: int, divisor: int) -> int:
    # your code here
    return 0


print("Example:")
print(find_remainder(3, 2))

# These "asserts" are used for self-checking
assert find_remainder(10, 3) == 1
assert find_remainder(14, 4) == 2
assert find_remainder(27, 4) == 3
assert find_remainder(10, 5) == 0
assert find_remainder(10, 1) == 0
assert find_remainder(5, 7) == 5
assert find_remainder(7, 5) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")