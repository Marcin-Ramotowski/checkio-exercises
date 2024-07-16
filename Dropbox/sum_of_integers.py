#!/usr/bin/env checkio --domain=py run sum-of-integers

# Calculate sum of integers from 1 to givenN(including).
# 
# 
# 
# Input:Integer(int).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert sum_upto_n(1) == 1
# assert sum_upto_n(2) == 3
# assert sum_upto_n(3) == 6
# assert sum_upto_n(4) == 10
# Precondition:1 ≤ N ≤ 900.
# 
# 
# END_DESC

def sum_upto_n(N: int) -> int:
    # your code here
    return 0


print("Example:")
print(sum_upto_n(11))

# These "asserts" are used for self-checking
assert sum_upto_n(1) == 1
assert sum_upto_n(2) == 3
assert sum_upto_n(3) == 6
assert sum_upto_n(4) == 10
assert sum_upto_n(5) == 15
assert sum_upto_n(10) == 55
assert sum_upto_n(20) == 210
assert sum_upto_n(100) == 5050
assert sum_upto_n(200) == 20100
assert sum_upto_n(500) == 125250

print("The mission is done! Click 'Check Solution' to earn rewards!")