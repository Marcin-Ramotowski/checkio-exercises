#!/usr/bin/env checkio --domain=py run number-with-exclamation

# This function should take a non-negative integer as an input and return the factorial of that number. The factorial of a non-negative integernis the product of all positive integers less than or equal ton.
# 
# 
# 
# Input:Integer(int).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert factorial(0) == 1
# assert factorial(1) == 1
# assert factorial(5) == 120
# assert factorial(10) == 3628800
# Precondition:n ∈ N₀
# 
# 
# END_DESC

def factorial(n: int) -> int:
    # your code here
    return 0


print("Example:")
print(factorial(4))

# These "asserts" are used for self-checking
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800
assert factorial(15) == 1307674368000

print("The mission is done! Click 'Check Solution' to earn rewards!")