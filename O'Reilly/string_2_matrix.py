#!/usr/bin/env checkio --domain=py run string-2-matrix

# You are given an unsorted string of unique (ignoring case) lower- and/or uppercase letters. Represent it as a correct mask for the square-arranged letters of the alphabet from "a" to "y" (row-major order). The mask must be a 5x5 matrix of integers as tuple of tuples with the following rule.character is not present in the string - use0in mask;character is lowercase - use1;character is uppercase - use2.
# 
# 
# 
# Here is a mission to make a reversed conversion -Matrix-2-String.
# 
# Input:String (str).
# 
# Output:Tuple of five tuples of five integers (int) each.
# 
# Examples:
# 
# assert converter("sMcigkqow") == (
#     (0, 0, 1, 0, 0),
#     (0, 1, 0, 1, 0),
#     (1, 0, 2, 0, 1),
#     (0, 1, 0, 1, 0),
#     (0, 0, 1, 0, 0),
# )
# assert converter("acSyIwoQkumGe") == (
#     (1, 0, 1, 0, 1),
#     (0, 2, 0, 2, 0),
#     (1, 0, 1, 0, 1),
#     (0, 2, 0, 2, 0),
#     (1, 0, 1, 0, 1),
# )
# Precondition:no "z" in string.
# 
# 
# END_DESC

Row = tuple[int, int, int, int, int]
Grid = tuple[Row, Row, Row, Row, Row]


def converter(text: str) -> Grid:
    # your code here
    return tuple()


print("Example:")
print(converter("sMcigkqow"))

# These "asserts" are used for self-checking
assert converter("sMcigkqow") == (
    (0, 0, 1, 0, 0),
    (0, 1, 0, 1, 0),
    (1, 0, 2, 0, 1),
    (0, 1, 0, 1, 0),
    (0, 0, 1, 0, 0),
)
assert converter("acSyIwoQkumGe") == (
    (1, 0, 1, 0, 1),
    (0, 2, 0, 2, 0),
    (1, 0, 1, 0, 1),
    (0, 2, 0, 2, 0),
    (1, 0, 1, 0, 1),
)

print("The mission is done! Click 'Check Solution' to earn rewards!")