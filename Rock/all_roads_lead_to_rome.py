#!/usr/bin/env checkio --domain=py run all-roads-lead-to-rome

# You are standing at the point(x, y)in thelatticegrid of pairs of non-negative numbers, and wish to make your way to the origin point(0, 0). At any point, you are allowed to move either one step left or one step down. Furthermore, you are never allowed to step into any of the points in thetabulist (origin is never intabu). This function should add up the number of different paths that lead from the point(x,y)to the origin(0,0)under these constraints.
# 
# If you feel yourself in need of a hint, here are two ideas of solving (click on a hint):
# 
# Hint 1This constrained variation of the classic combinatorial problem turns out to  have a reasonably straightforward recursive solution. As the base case, the number of paths from the origin(0, 0)to itself equals one for the empty path (note the crucial difference between an empty path that exists, versus a nonexistent path!). If the point(x, y)is in thetabulist, the number of paths from that point to the origin equals zero. Otherwise, the number of paths from the point to the origin equals the sum of paths from the two neighbors (x-1, y) and (x, y-1). However, this simple recursion branches into an exponential number of possibilities and may therefore  be  far too slow to execute. Therefore, you should either memoize the recursion withlru_cache, or even better...
# 
# Hint 2
# 
# Do not use recursion at all but build up a two-dimensional list whose entries are the individual subproblem solutions. Fill in the correct values with two for-loops in some order that guarantees that when these loops arrive at position [x][y], the results for positions [x-1][y] and [x][y-1] needed to compute [x][y] are already there.
# 
# Input:positionastupleof two integers(int)andtabuaslistof positions.
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert lattice_paths((3, 3), []) == 20
# assert lattice_paths((3, 4), [(2, 2)]) == 17
# assert lattice_paths((10, 5), [(6, 1), (2, 3)]) == 2063
# Precondition:x >= 0 and y >= 0.
# 
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def lattice_paths(position: tuple[int, int], tabu: list[tuple[int, int]]) -> int:
    # your code here
    return 0


print("Example:")
print(lattice_paths((3, 3), []))

# These "asserts" are used for self-checking
assert lattice_paths((3, 3), []) == 20
assert lattice_paths((3, 4), [(2, 2)]) == 17
assert lattice_paths((10, 5), [(6, 1), (2, 3)]) == 2063

print("The mission is done! Click 'Check Solution' to earn rewards!")