#!/usr/bin/env checkio --domain=py run the-longest-palindromic

# Write a function that finds the longestpalindromicsubstring of a given string. Try to be as efficient as possible!
# 
# If you find more than one substring, you should return the one that’s closer to the beginning.
# 
# Input:A text as a string.
# 
# Output:The longest palindromic substring.
# 
# Precondition:1 < |text| ≤ 20
# The text contains only ASCII characters.
# 
# 
# END_DESC

def longest_palindromic(text: str) -> str:
    n = len(text)
    for x in range(n, 0, -1):
        for i in range(0, n-x+1):
            substring = text[i:i+x]
            if substring == substring[::-1]:
                return substring
    return max(text)