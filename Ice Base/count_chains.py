#!/usr/bin/env checkio --domain=py run count-chains

# In this mission you must count chains.
# 
# You are given a list of details of the circle (tuple of X-coordinate, Y-coordinate, radius).
# You have to return the number of groups of circles where their circumferences intersect.
# 
# NOTE:
# 
# Only one circle counts as one group.
# 
# Input:A list of details of the circle.Details of the circle is a tuple of three integers(X-coordinate, Y-coordinate, radius).
# 
# Output:An integer.
# 
# Precondition:
# -10 ≤ x(, y) coordinate ≤ 101 ≤ radius ≤ 10
# 
# 
# END_DESC

from sympy.geometry import Circle
from sympy.geometry.util import intersection

def count_chains(coords):
    circles = [Circle((x, y), r) for x, y, r in sorted(coords)]
    def close(circle):
        for other in circles:
            if len(intersection(other, circle)) > 1:
                circles.remove(other)
                close(other)
    chains = 0
    while circles:
        chains += 1
        close(circles.pop())
    return chains



if __name__ == '__main__':
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")