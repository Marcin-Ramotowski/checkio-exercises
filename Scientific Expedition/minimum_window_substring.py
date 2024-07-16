#!/usr/bin/env checkio --domain=py run minimum-window-substring

# Given a stringlineand a patternpattern, write a function to find the minimum window substring of thelinethat contains at least all the characters of thepattern(may contain other characters also). The order of the characters in theline/patterndoesn't matter, but the letter case does.
# 
# Your function should return a tuple of starting and ending indexes oflinewhich form the needed window (right border is excluded). If there is no such substring inlineto matchpattern, return(-1, -1).
# 
# 
# 
# Input:Two strings(str).
# 
# Output:Tuple of two integers(int).
# 
# Examples:
# 
# assert window("ADOBECODEBANC", "ABC") == (9, 13)
# assert window("ab", "a") == (0, 1)
# assert window("ab", "A") == (-1, -1)
# assert window("abcdef", "ace") == (0, 5)
# Precondition:all letters in pattern are unique.
# 
# 
# END_DESC

def window(line: str, pattern: str) -> tuple[int, int]:
    # your code here
    return -1, -1


print("Example:")
print(window("ADOBECODEBANC", "ABC"))

# These "asserts" are used for self-checking
assert window("ADOBECODEBANC", "ABC") == (9, 13)
assert window("ab", "a") == (0, 1)
assert window("ab", "A") == (-1, -1)
assert window("abcdef", "ace") == (0, 5)
assert window("MixEdCaSeScRiNgTrIcKy", "cSeR") == (8, 12)

print("The mission is done! Click 'Check Solution' to earn rewards!")