#!/usr/bin/env checkio --domain=py run interesting-intersecting

# A square on the two-dimensional plane can be defined as a tuple(x, y, l), where(x, y)are the coordinates of itsbottom left cornerandlis the length of the side of the square (we only consider squares that are aligned to the axes). Given two squares as tuples(x1, y1, l1)and(x2, y2, l2), your function should determine whether these two squaresintersect, that is, theirareashave at least one point in common, even if that one point is merely the shared corner point when these two squares are placed kitty corner.
# 
# We also prepared a stick and a carrot for you:
# 
# try to write this missionwith no loops or list comprehensions of any kind, but should compute the result using only integer comparisons and conditional statements;
# 
# it is actually much easier to determine that the two squares donotintersect, and then negate that answer. Two squares do not intersect if one of them ends in the horizontal direction before the other one begins, or if the same thing happens in the vertical direction.
# 
# Input:Two tuples with three integers in each.
# 
# Output:Bool.
# 
# Examples:
# 
# assert squares_intersect((2, 2, 3), (5, 5, 2)) == True
# assert squares_intersect((3, 6, 1), (8, 3, 5)) == False
# assert squares_intersect((3000, 6000, 1000), (8000, 3000, 5000)) == False
# This task is taken from the course CCPS 109 Computer Science I, as taught byIlkka Kokkarinen.
# 
# 
# END_DESC

def squares_intersect(s1: tuple[int, int, int], s2: tuple[int, int, int]) -> bool:
    return not((s1[0] + s1[2] < s2[0]) or (s1[1] + s1[2] < s2[1]))

if __name__ == '__main__':
    print("Example:")
    print(squares_intersect((2, 2, 3), (5, 5, 2)))

    assert squares_intersect((2, 2, 3), (5, 5, 2)) == True
    assert squares_intersect((3, 6, 1), (8, 3, 5)) == False
    assert squares_intersect((3000, 6000, 1000), (8000, 3000, 5000)) == False

    print("The mission is done! Click 'Check Solution' to earn rewards!")