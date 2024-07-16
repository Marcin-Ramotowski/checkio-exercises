#!/usr/bin/env checkio --domain=py run matrix-2-string

# You are given a 5x5 matrix of integers as tuple of tuples. Use it as a mask for the square-arranged letters of the alphabet from "a" to "y" (row-major order). Return a string of characters (sorted, ignore case), picked from the square of letters according to the mask with the following rule:0in mask - do not take the respective character;1- take in lowercase;2- take in uppercase.
# 
# 
# 
# Here is a mission to make a reverse conversion -String-2-Matrix.
# 
# Input:Tuple of five tuples of five integers (int) each.
# 
# Output:String (str).
# 
# Examples:
# 
# assert (
#     converter(
#         (
#             (0, 0, 1, 0, 0),
#             (0, 1, 0, 1, 0),
#             (1, 0, 2, 0, 1),
#             (0, 1, 0, 1, 0),
#             (0, 0, 1, 0, 0),
#         )
#     )
#     == "cgikMoqsw"
# )
# assert (
#     converter(
#         (
#             (1, 0, 1, 0, 1),
#             (0, 2, 0, 2, 0),
#             (1, 0, 1, 0, 1),
#             (0, 2, 0, 2, 0),
#             (1, 0, 1, 0, 1),
#         )
#     )
#     == "aceGIkmoQSuwy"
# )
# 
# END_DESC

Row = tuple[int, int, int, int, int]
Grid = tuple[Row, Row, Row, Row, Row]


def converter(matrix: Grid) -> str:
    # your code here
    return ""


print("Example:")
print(
    converter(
        (
            (0, 0, 1, 0, 0),
            (0, 1, 0, 1, 0),
            (1, 0, 2, 0, 1),
            (0, 1, 0, 1, 0),
            (0, 0, 1, 0, 0),
        )
    )
)

# These "asserts" are used for self-checking
assert (
    converter(
        (
            (0, 0, 1, 0, 0),
            (0, 1, 0, 1, 0),
            (1, 0, 2, 0, 1),
            (0, 1, 0, 1, 0),
            (0, 0, 1, 0, 0),
        )
    )
    == "cgikMoqsw"
)
assert (
    converter(
        (
            (1, 0, 1, 0, 1),
            (0, 2, 0, 2, 0),
            (1, 0, 1, 0, 1),
            (0, 2, 0, 2, 0),
            (1, 0, 1, 0, 1),
        )
    )
    == "aceGIkmoQSuwy"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")