#!/usr/bin/env checkio --domain=py run factorial-zeros

# Write a function that finds the number of zeros at the end of the decimal expansion of factorialn!. Because factorials grow very fast, it is not a good strategy to calculaten!and count the zeros.
# 
# 
# 
# Input:Integer(int).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert fact_zeros(2) == 0
# assert fact_zeros(5) == 1
# assert fact_zeros(20) == 4
# This mission was taken fromWOLFRAM CHALLENGES
# 
# 
# END_DESC

def fact_zeros(n: int) -> int:
    # your code here
    return 0


print("Example:")
print(fact_zeros(2))

# These "asserts" are used for self-checking
assert fact_zeros(2) == 0
assert fact_zeros(5) == 1
assert fact_zeros(20) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")