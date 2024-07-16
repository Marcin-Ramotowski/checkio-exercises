#!/usr/bin/env checkio --domain=py run bishop-vs-aliens

# A lone chess bishop finds himself standing on the (zero-based indexing) square(x, y)of a curiousm * nchessboard floating in outer space, covered with completely frictionless magic ice. This board is not necessarily square, but can be any rectangle of integer dimensions. The board is surrounded from all sides with bouncy walls similar to an air hockey table. Some of the squares on the board containaliensthat make game over man for anyone who enters that square.
# 
# The bishop can initially propel himself to any of the four diagonal directions. After this initial impulse gets him going, the bishop can no longer control his movements on the frictionless ice, but will keep sliding towards whatever end the present direction vector and bouncing from the walls take him. It is even possible for the bishop to forever repeat the same cycle of squares.
# 
# The bishop must reach any one of the four possible exits at the four corners of the board. This function should determine whether there exists at least one starting direction that leads the bishop to the safety of any one of the four corners, avoiding all thealiensalong the way. Look at the examplex = 3, y = 2, m = 4, n = 5, aliens = [(2, 2), (1, 4)]=>True.
# 
# 
# 
# Input:Four integers(int)andlistof tuples of two integers.
# 
# Output:Logic value(bool).
# 
# Examples:
# 
# assert reach_corner(0, 2, 5, 5, []) == False
# assert reach_corner(4, 4, 9, 9, [(0, 0), (0, 8), (8, 0), (8, 8)]) == False
# assert reach_corner(1, 1, 1000, 2, [(0, 0), (0, 1), (999, 0)]) == True
# Preconditions:0 <= x < m, 0 <= y < n;m > 1, n > 1;(x,y) not in aliens.
# 
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def reach_corner(x: int, y: int, m: int, n: int, aliens: list[tuple[int, int]]) -> bool:
    # your code here
    return False


print("Example:")
print(reach_corner(0, 2, 5, 5, []))

# These "asserts" are used for self-checking
assert reach_corner(0, 2, 5, 5, []) == False
assert reach_corner(4, 4, 9, 9, [(0, 0), (0, 8), (8, 0), (8, 8)]) == False
assert reach_corner(1, 1, 1000, 2, [(0, 0), (0, 1), (999, 0)]) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")