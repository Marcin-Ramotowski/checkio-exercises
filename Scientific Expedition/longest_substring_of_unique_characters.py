#!/usr/bin/env checkio --domain=py run longest-substring-of-unique-characters

# Given a string, find the length of the longest substring without repeating characters.
# 
# 
# 
# Input:String(str).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert longest_substr("abcabcbb") == 3
# assert longest_substr("bbbbb") == 1
# assert longest_substr("pwwkew") == 3
# assert longest_substr("abcdef") == 6
# 
# END_DESC

def longest_substr(s: str) -> int:
    # your code here
    return 0


print("Example:")
print(longest_substr("abcabcbb"))

# These "asserts" are used for self-checking
assert longest_substr("abcabcbb") == 3
assert longest_substr("bbbbb") == 1
assert longest_substr("pwwkew") == 3
assert longest_substr("abcdef") == 6
assert longest_substr("") == 0
assert longest_substr("au") == 2
assert longest_substr("dvdf") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")