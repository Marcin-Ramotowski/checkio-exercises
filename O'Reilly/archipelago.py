#!/usr/bin/env checkio --domain=py run archipelago

# Did you know, that Stockholm is a city built on 14 islands, connected by 57 bridges over the two waters Lake Mälaren and the Baltic Sea.
# 
# You are given a rectangular map of islands where the number in each island tells how many bridges are connected to it.
# 
# 
# 
# The object is to connect all islands according to the number of bridges with the following rules:there are no more than two bridges in the same direction;bridges can only be vertical or horizontal and can't cross islands or other bridges;when completed, all island on a map are interconnected by bridges, enabling passage from any island to another.
# 
# Your function must return a sorted ascending tuple of directions with bridges. Each direction is a tuple itself with three integers. The first two are serial numbers of islands (sorted ascending), the third one is number of bridges between these two islands (1 or 2). Islands must be ordered starting from 1, from top-left to bottom-right, row-major.
# 
# 
# 
# Input:Tuple of tuples of integers(int).
# 
# Output:Tuple of tuples of three integers(int).
# 
# Examples:
# 
# assert archipelago(
#     (
#         (0, 1, 0, 0, 2),
#         (2, 0, 0, 2, 0),
#         (0, 0, 2, 0, 2),
#         (0, 0, 0, 1, 0),
#         (3, 0, 6, 0, 3),
#     )
# ) == (
#     (1, 2, 1),
#     (2, 6, 1),
#     (3, 4, 1),
#     (3, 8, 1),
#     (4, 7, 1),
#     (5, 9, 2),
#     (6, 10, 1),
#     (8, 9, 2),
#     (9, 10, 2),
# )  # very easy, 5x5
# assert archipelago(
#     (
#         (3, 0, 6, 0, 3),
#         (0, 1, 0, 0, 0),
#         (2, 0, 2, 0, 0),
#         (0, 2, 0, 0, 3),
#         (5, 0, 3, 0, 0),
#         (0, 0, 0, 0, 1),
#         (2, 0, 1, 0, 0),
#     )
# ) == (
#     (1, 2, 2),
#     (1, 5, 1),
#     (2, 3, 2),
#     (2, 6, 2),
#     (3, 8, 1),
#     (4, 7, 1),
#     (5, 9, 1),
#     (7, 8, 1),
#     (8, 11, 1),
#     (9, 10, 2),
#     (9, 12, 2),
#     (10, 13, 1),
# )  # very easy, 5x7
# assert archipelago(
#     (
#         (0, 2, 0, 0, 2, 0),
#         (2, 0, 2, 0, 0, 0),
#         (0, 1, 0, 0, 0, 2),
#         (5, 0, 8, 0, 3, 0),
#         (0, 0, 0, 0, 0, 0),
#         (1, 0, 3, 0, 0, 3),
#     )
# ) == (
#     (1, 2, 1),
#     (1, 5, 1),
#     (2, 9, 1),
#     (3, 7, 2),
#     (4, 8, 2),
#     (6, 12, 2),
#     (7, 8, 2),
#     (7, 10, 1),
#     (8, 9, 2),
#     (8, 11, 2),
#     (11, 12, 1),
# )  # very easy, 6x6
# Precondition:all tests are solvable and have one solution.
# 
# This mission is an implementation of the followingHashi Google Play app. All tests are the first ones from their kinds (difficulty and dimensions). I strongly recommend you to use the app to understand the mission better and solve it easier as I did while creating it.
# 
# 
# END_DESC

def archipelago(data: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, int, int], ...]:
    # your code here
    return []


print("Example:")
print(
    archipelago(
        (
            (0, 1, 0, 0, 2),
            (2, 0, 0, 2, 0),
            (0, 0, 2, 0, 2),
            (0, 0, 0, 1, 0),
            (3, 0, 6, 0, 3),
        )
    )
)

# These "asserts" are used for self-checking
assert archipelago(
    (
        (0, 1, 0, 0, 2),
        (2, 0, 0, 2, 0),
        (0, 0, 2, 0, 2),
        (0, 0, 0, 1, 0),
        (3, 0, 6, 0, 3),
    )
) == (
    (1, 2, 1),
    (2, 6, 1),
    (3, 4, 1),
    (3, 8, 1),
    (4, 7, 1),
    (5, 9, 2),
    (6, 10, 1),
    (8, 9, 2),
    (9, 10, 2),
)  # very easy, 5x5
assert archipelago(
    (
        (3, 0, 6, 0, 3),
        (0, 1, 0, 0, 0),
        (2, 0, 2, 0, 0),
        (0, 2, 0, 0, 3),
        (5, 0, 3, 0, 0),
        (0, 0, 0, 0, 1),
        (2, 0, 1, 0, 0),
    )
) == (
    (1, 2, 2),
    (1, 5, 1),
    (2, 3, 2),
    (2, 6, 2),
    (3, 8, 1),
    (4, 7, 1),
    (5, 9, 1),
    (7, 8, 1),
    (8, 11, 1),
    (9, 10, 2),
    (9, 12, 2),
    (10, 13, 1),
)  # very easy, 5x7
assert archipelago(
    (
        (0, 2, 0, 0, 2, 0),
        (2, 0, 2, 0, 0, 0),
        (0, 1, 0, 0, 0, 2),
        (5, 0, 8, 0, 3, 0),
        (0, 0, 0, 0, 0, 0),
        (1, 0, 3, 0, 0, 3),
    )
) == (
    (1, 2, 1),
    (1, 5, 1),
    (2, 9, 1),
    (3, 7, 2),
    (4, 8, 2),
    (6, 12, 2),
    (7, 8, 2),
    (7, 10, 1),
    (8, 9, 2),
    (8, 11, 2),
    (11, 12, 1),
)  # very easy, 6x6

print("The mission is done! Click 'Check Solution' to earn rewards!")