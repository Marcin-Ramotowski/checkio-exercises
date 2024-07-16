#!/usr/bin/env checkio --domain=py run reverse-integer

# Reverse the digits of a given integer. For instance,1234should become4321. For negative integers, the sign should remain in the front; e.g.,-123becomes-321.
# 
# 
# 
# Input:Integer(int).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert reverse_digits(1234) == 4321
# assert reverse_digits(0) == 0
# assert reverse_digits(-123) == -321
# assert reverse_digits(5) == 5
# Precondition:−109≤ num ≤ 109.
# 
# 
# END_DESC

def reverse_digits(num: int) -> int:
    # your code here
    return 0


print("Example:")
print(reverse_digits(32))

# These "asserts" are used for self-checking
assert reverse_digits(1234) == 4321
assert reverse_digits(0) == 0
assert reverse_digits(-123) == -321
assert reverse_digits(5) == 5
assert reverse_digits(-9) == -9
assert reverse_digits(100) == 1
assert reverse_digits(-100) == -1
assert reverse_digits(54321) == 12345
assert reverse_digits(1111) == 1111
assert reverse_digits(987654321) == 123456789

print("The mission is done! Click 'Check Solution' to earn rewards!")