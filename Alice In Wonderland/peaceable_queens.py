#!/usr/bin/env checkio --domain=py run peaceable-queens

# This task is adapted from following video with Neil Sloane (founder of theOn-Line Encyclopedia of Integer Sequences), that you should watch first to learn, how this excellent puzzle works.
# 
# 
# 
# You are given a chessboard of custom dimension:size * size. Your goal is to put there as many ♕ and ♛ as possible with these rules of placement:only equal numbers of Queens are allowed;♕ must not attack ♛ and vice versa (but they may be under "attack" of the same color Queens).
# 
# Your function should return the maximum number of opposite Queens pairs, you could put on the given chessboard according to the restrictions.
# 
# Input:Size of the chessboard as integer.
# 
# Output:Maximum number of opposite Queens pairs as integer.
# 
# Examples:
# 
# assert peaceable_queens(1) == 0
# assert peaceable_queens(2) == 0
# assert peaceable_queens(3) == 1
# assert peaceable_queens(4) == 2
# 
# END_DESC

def peaceable_queens(size: int) -> int:
    # your code here
    return 0


print("Example:")
print(peaceable_queens(3))

# These "asserts" are used for self-checking
assert peaceable_queens(1) == 0
assert peaceable_queens(2) == 0
assert peaceable_queens(3) == 1
assert peaceable_queens(4) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")