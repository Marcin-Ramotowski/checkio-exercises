#!/usr/bin/env checkio --domain=py run count-squares

# This problem is adapted fromCount the Number of Squaresat Wolfram Challenges, so you might want to first check out that page for illustrative visualizations of this problem.
# 
# Given a sequence of points (coordinatesx, yas nonnegative integers), your function should count how many squares exist so that all four corners are members of points. Note that these squares are not required to be axis-aligned so that their sides would have to be either horizontal and vertical. For example, the points(0, 3), (3, 0), (6, 3), (3, 6)define a square, even if it may happen to look like a lozenge from our axis-aligned vantage point.
# 
# By the way, if your want to try another approach and count squares, having lines between points,The Square Chestawaits you!
# 
# Input:Listof tuples(tuple)of two integers (int).
# 
# Output:Integer (int).
# 
# Examples:
# 
# assert count_squares([(0, 0), (1, 0), (0, 1), (1, 1)]) == 1
# assert (
#     count_squares(
#         [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
#     )
#     == 6
# )
# assert (
#     count_squares(
#         [
#             (4, 3),
#             (1, 1),
#             (5, 3),
#             (2, 3),
#             (3, 2),
#             (3, 1),
#             (4, 2),
#             (2, 1),
#             (3, 3),
#             (1, 2),
#             (5, 2),
#         ]
#     )
#     == 3
# )
# If you feel yourself in need of additional chapter of explanation (tip), press this line.To identify four points that constitute a square, note how every square has bottom left corner pointx, yand direction vectordx, dytowards its upper left corner point that satisfiesdx >= 0 & dy > 0, so that the points(x+dx,y+dy), (x+dy,y-dx), (x+dx+dy,y-dx+dy)for the top left, bottom right and top right corners of that square, respectively, are also included in points. You can therefore (effectively) iterate through all possibilities for the bottom left point and the direction vector and be guaranteed to find all squares in the grid.
# 
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def count_squares(points: list[tuple[int, int]]) -> int:
    # your code here
    return 0


print("Example:")
print(count_squares([(0, 0), (1, 0), (0, 1), (1, 1)]))

# These "asserts" are used for self-checking
assert count_squares([(0, 0), (1, 0), (0, 1), (1, 1)]) == 1
assert (
    count_squares(
        [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
    )
    == 6
)
assert (
    count_squares(
        [
            (4, 3),
            (1, 1),
            (5, 3),
            (2, 3),
            (3, 2),
            (3, 1),
            (4, 2),
            (2, 1),
            (3, 3),
            (1, 2),
            (5, 2),
        ]
    )
    == 3
)

print("The mission is done! Click 'Check Solution' to earn rewards!")