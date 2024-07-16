#!/usr/bin/env checkio --domain=py run armstrong-number-checking

# In number theory, anArmstrongnumber(afterMichael F. Armstrong) ornarcissistic numberin a given number base (10 for this mission) is a number that is the sum of its own digits each raised to the power of the number of digits. For example, 153 is anArmstrongnumber because13+ 53+ 33== 153.
# 
# 
# 
# Input:Integer(int).
# 
# Output:Logic value(bool).
# 
# Examples:
# 
# assert is_armstrong(153) == True
# assert is_armstrong(370) == True
# assert is_armstrong(947) == False
# assert is_armstrong(371) == True
# 
# END_DESC

def is_armstrong(num: int) -> bool:
    # your code here
    return False


print("Example:")
print(is_armstrong(11))

# These "asserts" are used for self-checking
assert is_armstrong(153) == True
assert is_armstrong(370) == True
assert is_armstrong(947) == False
assert is_armstrong(371) == True
assert is_armstrong(407) == True
assert is_armstrong(163) == False
assert is_armstrong(100) == False
assert is_armstrong(8208) == True
assert is_armstrong(930) == False
assert is_armstrong(4) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")