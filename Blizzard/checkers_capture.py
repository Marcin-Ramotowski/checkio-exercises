#!/usr/bin/env checkio --domain=py run checkers-capture

# Imagine an-by-nchessboard, where your single checker currently stands atposition(x, y) and there ispieces- a list that contains the positions of the opponent’s pawns.
# 
# Your checker may capture a piece only one step in the four diagonal directions assuming that the square behind the opponent piece in that diagonal direction is vacant. Your checker can then capture that piece by jumping over it into the vacant square, immediately removing that captured piece from the board. The chain of captures continues from the new square, potentially capturing all the pieces in one swoop.
# 
# Your function should return the maximum number of pieces that your checker could potentially capture in a single move.
# 
# Input:Three arguments: size(int), coordinates (tupleof two integers(int)) and a sequence of opponent's pieces (listof coordinates).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert max_checkers_capture(5, (0, 2), [(1, 1), (3, 1), (1, 3)]) == 2
# assert max_checkers_capture(7, (0, 0), [(1, 1), (1, 3), (3, 3), (2, 4), (1, 5)]) == 3
# assert (
#     max_checkers_capture(
#         8,
#         (5, 3),
#         [
#             (6, 2),
#             (2, 4),
#             (2, 2),
#             (0, 4),
#             (5, 5),
#             (1, 5),
#             (3, 7),
#             (6, 4),
#             (5, 7),
#             (0, 6),
#             (0, 2),
#             (1, 7),
#             (2, 6),
#             (6, 0),
#             (6, 6),
#             (3, 5),
#         ],
#     )
#     == 1
# )
# Need a small hint? Click onThe maximum number of pieces that can be captured in a single move is best computed with a method that locally loops through the four diagonal directions from the current position of the king. For each such direction that contains an opponent piece with a vacant space behind it, remove that opponent piece from the board, and recursively compute the number of pieces that can be captured from the vacant square that your king jumps into. Once that recursive call has returned, restore the captured piece on the board, and continue looping to the next diagonal direction. The number of captures of whichever direction gives the best result from that square is returned as the answer.
# 
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def max_checkers_capture(
    n: int, position: tuple[int, int], pieces: list[tuple[int, int]]
) -> int:
    # your code here
    return 0


print("Example:")
print(max_checkers_capture(5, (0, 2), [(1, 1), (3, 1), (1, 3)]))

# These "asserts" are used for self-checking
assert max_checkers_capture(5, (0, 2), [(1, 1), (3, 1), (1, 3)]) == 2
assert max_checkers_capture(7, (0, 0), [(1, 1), (1, 3), (3, 3), (2, 4), (1, 5)]) == 3
assert (
    max_checkers_capture(
        8,
        (5, 3),
        [
            (6, 2),
            (2, 4),
            (2, 2),
            (0, 4),
            (5, 5),
            (1, 5),
            (3, 7),
            (6, 4),
            (5, 7),
            (0, 6),
            (0, 2),
            (1, 7),
            (2, 6),
            (6, 0),
            (6, 6),
            (3, 5),
        ],
    )
    == 1
)

print("The mission is done! Click 'Check Solution' to earn rewards!")