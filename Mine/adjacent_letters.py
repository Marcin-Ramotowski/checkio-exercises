#!/usr/bin/env checkio --domain=py run adjacent-letters

# You are given a string, where all letters are of same case. This string could    include adjacent letters - two the same letters together ("aa", "bb" etc).    Your task in this mission is to remove both these letters. If after removing    one pair a new appears - remove it as well! Each such pair should be removed    from string until no one remains. Good luck!
# 
# Input:String(str).
# 
# Output:String(str).
# 
# Examples:
# 
# assert adjacent_letters("adjacent_letters") == "adjacent_lrs"
# assert adjacent_letters("") == ""
# assert adjacent_letters("aaa") == "a"
# assert adjacent_letters("ABBA") == ""
# 
# END_DESC

import string


def adjacent_letters(line: str) -> str:
    LETTERS = string.ascii_letters
    for letter in LETTERS:
        adj = letter * 2
        if adj in line:
            line = line.replace(adj, '')
            return adjacent_letters(line)
    return line


print("Example:")
print(adjacent_letters("abbaca"))

assert adjacent_letters("adjacent_letters") == "adjacent_lrs"
assert adjacent_letters("") == ""
assert adjacent_letters("aaa") == "a"
assert adjacent_letters("ABBA") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")