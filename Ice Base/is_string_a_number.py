#!/usr/bin/env checkio --domain=py run is-string-a-number

# You are given a string. Your function should returnTrueif the string is a valid number (contains digits only), otherwise -False. Look at the example.
# 
# 
# 
# Input:A string.
# 
# Output:A boolean.
# 
# Precondition:The text contains only letters, digits and whitespace.
# 
# 
# END_DESC

def is_number(val: str) -> bool:
    # your code here
    return val.is


print("Example:")
print(is_number("34"))

# These "asserts" are used for self-checking
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("a5") == False
assert is_number("ITS A NUMBER") == False
assert is_number("5a") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")