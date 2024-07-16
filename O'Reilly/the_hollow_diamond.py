#!/usr/bin/env checkio --domain=py run the-hollow-diamond

# Your function should return a multiline string of unique lowercase letters in alphabetical order. The characters should be placed in a form of hollow rhombus (diamond), along its edges, starting from the top vertex.
# 
# For this purpose you are given three values (for their constraints see Preconditions):side- number of letters in each side of the rhombus;length- total number of letters you should use;cw- clockwise flag, which shows in what direction the letters must go (ifTrue- letters should be placed in clockwise direction).
# 
# If it's not enoughlengthto complete the form, complement it with"*". The rhombus should not have white spaces at the right. Here is an example with arguments and expected result:
# 
# 
# 
# Input:Three arguments: side as integer (int), length as integer (int) and clockwise flag as logic (bool).
# 
# Output:Multiline string(str).
# 
# Examples:
# 
# assert hollow_diamond(3, 8, True) == "  a\n h b\ng   c\n f d\n  e"
# assert hollow_diamond(3, 6, False) == "  a\n b *\nc   *\n d f\n  e"
# assert (
#     hollow_diamond(4, 10, False) == "   a\n  b *\n c   *\nd     j\n e   i\n  f h\n   g"
# )
# assert (
#     hollow_diamond(5, 16, True)
#     == "    a\n   p b\n  o   c\n n     d\nm       e\n l     f\n  k   g\n   j h\n    i"
# )
# Preconditions:26 >= length >= 0;side > 1;(side-1)*4 >= length.
# 
# 
# END_DESC

def hollow_diamond(side: int, length: int, cw: bool) -> str:
    # your code here
    return ""


print("Example:")
print(hollow_diamond(3, 6, False))

# These "asserts" are used for self-checking
assert hollow_diamond(3, 8, True) == "  a\n h b\ng   c\n f d\n  e"
assert hollow_diamond(3, 6, False) == "  a\n b *\nc   *\n d f\n  e"
assert (
    hollow_diamond(4, 10, False) == "   a\n  b *\n c   *\nd     j\n e   i\n  f h\n   g"
)
assert (
    hollow_diamond(5, 16, True)
    == "    a\n   p b\n  o   c\n n     d\nm       e\n l     f\n  k   g\n   j h\n    i"
)
assert (
    hollow_diamond(5, 14, False)
    == "    a\n   b *\n  c   *\n d     n\ne       m\n f     l\n  g   k\n   h j\n    i"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")