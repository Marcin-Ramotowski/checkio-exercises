#!/usr/bin/env checkio --domain=py run fuzzy-string-matching

# Given two strings and a permissible number of character differences, determine if the strings can be considered approximately equal.
# 
# 
# 
# Input:Three arguments: two strings(str)and one integer(int).
# 
# Output:Logic value(bool).
# 
# Examples:
# 
# assert fuzzy_string_match("apple", "appel", 2) == True
# assert fuzzy_string_match("apple", "bpple", 1) == True
# assert fuzzy_string_match("apple", "bpple", 0) == False
# assert fuzzy_string_match("apple", "apples", 1) == True
# Precondition:0 <= threshold <= max(len(str1), len(str2)).
# 
# 
# END_DESC

def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    # your code here
    return False


print("Example:")
print(fuzzy_string_match("apple", "appel", 2))

# These "asserts" are used for self-checking
assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True
assert fuzzy_string_match("apple", "bpples", 2) == True
assert fuzzy_string_match("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")