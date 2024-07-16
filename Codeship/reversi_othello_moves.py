#!/usr/bin/env checkio --domain=py run reversi-othello-moves

# 
# 
# Reversiis a strategy board game for two players, played on an 8×8 uncheckered board. It was invented in 1883. Othello, a variant with a fixed initial setup of the board, was patented in 1971.
# 
# For the purposes of this mission you need to write a move generator to find all moves available for Othello against Desdemona on the given board. The game pieces of Othello (⚫) and Desdemona (⚪) on the board are lists of tuples of theirx- andy-coordinates, both ranging from 0 to 7.
# 
# This function should return a list of all possible moves available to Othello. The returned moves must be encoded as tuples(x, y, flips)wherex, yare the coordinates of the move, followed by the count of how many of Desdemona’s pieces that particular move would flip into Othello’s pieces.
# 
# To make the expected correct answer unique, the returned list of moves must be sorted in descending order of flips. Moves that flip the same number of pieces should be listed in ascending order of theirx-coordinates, breaking the ties with they-coordinate also in ascending order.
# 
# Input:Two lists of tuples of 2 integers.
# 
# Output:List of tuples of 3 integers.
# 
# Examples:
# 
# assert othello_moves([(3, 3), (4, 4)], [(3, 4), (4, 3), (2, 3)]) == [
#     (1, 3, 1),
#     (2, 4, 1),
#     (3, 5, 1),
#     (4, 2, 1),
#     (5, 3, 1),
# ]
# assert othello_moves([(3, 3), (4, 4), (2, 3), (2, 5)], [(3, 4), (4, 3), (2, 4)]) == [
#     (1, 4, 2),
#     (5, 2, 2),
#     (1, 5, 1),
#     (3, 5, 1),
#     (4, 2, 1),
#     (4, 5, 1),
#     (5, 3, 1),
# ]
# This task is taken from the course CCPS 109 Computer Science I, Version of December 21, 2022, as taught byIlkka Kokkarinen.
# 
# 
# END_DESC

def othello_moves(
    othello: list[tuple[int, int]], desdemona: list[tuple[int, int]]
) -> list[tuple[int, int, int]]:
    # your code here
    return []


print("Example:")
print(othello_moves([(3, 3), (4, 4)], [(3, 4), (4, 3), (2, 3)]))

# These "asserts" are used for self-checking
assert othello_moves([(3, 3), (4, 4)], [(3, 4), (4, 3), (2, 3)]) == [
    (1, 3, 1),
    (2, 4, 1),
    (3, 5, 1),
    (4, 2, 1),
    (5, 3, 1),
]
assert othello_moves([(3, 3), (4, 4), (2, 3), (2, 5)], [(3, 4), (4, 3), (2, 4)]) == [
    (1, 4, 2),
    (5, 2, 2),
    (1, 5, 1),
    (3, 5, 1),
    (4, 2, 1),
    (4, 5, 1),
    (5, 3, 1),
]

print("The mission is done! Click 'Check Solution' to earn rewards!")