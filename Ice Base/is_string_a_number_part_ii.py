#!/usr/bin/env checkio --domain=py run is-string-a-number-part-ii

# You are given a string. Your function should returnTrueif the string is a valid number (contains only digits and "+-." at proper places), otherwise -False. Look at the mask:
# 
# 
# [+- ][zero or more digits][.][zero or more digits]
# Of course, not all parts are necessary (but at least one digit part is!). For example, "+10." or "-.55" are valid numbers, where part equal 0 is omitted.
# 
# Input:A string(str).
# 
# Output:Logic value(bool).
# 
# Examples:
# 
# assert is_number("34") == True
# assert is_number("df") == False
# assert is_number("") == False
# assert is_number("+10.0") == True
# 
# END_DESC

def is_number(val: str) -> bool:
    # your code here
    return False


print("Example:")
print(is_number("10"))

# These "asserts" are used for self-checking
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("+10.0") == True
assert is_number("1OOO") == False
assert is_number("1.") == True
assert is_number("+.l") == False
assert is_number("++1+.2-") == False
assert is_number("3e4") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")