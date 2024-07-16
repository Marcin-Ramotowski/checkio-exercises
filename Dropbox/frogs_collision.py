#!/usr/bin/env checkio --domain=py run frogs-collision

# A frog hopping along on the infinite two-dimensional grid of integers is represented as a 4-tuple of the form(x, y, dx, dy)so thatx, yis the frog’s starting position at timet = 0, anddx, dyis its constant direction vector for each hop. Time advances in discrete integer steps so that each frog makes one hop at every tick of the clock.
# 
# Given two frogsfrog1, frog2, that initially stand on different squares, return the time when both frogs hop into the same square. If these two frogs never hop into the same square at the same time, this function should returnNone.
# 
# Let's look at the example(0, 0, 0, 2), (0, 10, 0, 1).X's are equal and don't change (dx1 == dx2 == 0), so we may ignore them.
# 
# 
# 
# Your function should not contain any loops whatsoever, but the result should be computed with conditional statements and integer arithmetic.
# 
# Input:Two tuples of four integersint.
# 
# Output:Integer or None.
# 
# Examples:
# 
# assert frogs_collision((0, 0, 0, 2), (0, 10, 0, 1)) == 10
# assert frogs_collision((10, 10, -1, 0), (0, 1, 0, 1)) == None
# assert (
#     frogs_collision(
#         (620775675217287, -1862327025651882, -3, 9),
#         (413850450144856, 2069252250724307, -2, -10),
#     )
#     == 206925225072431
# )
# assert frogs_collision((0, 0, 0, 0), (1, 1, 3, 3)) == None
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

Frog = tuple[int, int, int, int]


def frogs_collision(frog1: Frog, frog2: Frog) -> int | None:
    # your code here
    return 0


print("Example:")
print(frogs_collision((0, 0, 0, 2), (0, 10, 0, 1)))

# These "asserts" are used for self-checking
assert frogs_collision((0, 0, 0, 2), (0, 10, 0, 1)) == 10
assert frogs_collision((10, 10, -1, 0), (0, 1, 0, 1)) == None
assert (
    frogs_collision(
        (620775675217287, -1862327025651882, -3, 9),
        (413850450144856, 2069252250724307, -2, -10),
    )
    == 206925225072431
)
assert frogs_collision((0, 0, 0, 0), (1, 1, 3, 3)) == None

print("The mission is done! Click 'Check Solution' to earn rewards!")