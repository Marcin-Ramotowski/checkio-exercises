#!/usr/bin/env checkio --domain=py run super-root

# Square roots, cube roots, 4th roots... each are too boring for Nicola.    He needs to find the super root! With your help he will almost certainly find it.
# 
# The super root of a numberNis the numberx,    such thatxx=N.
# 
# The result should be accurate so thatxx≈ N±0.001.    OrN - 0.001 < xx< N + 0.001.
# 
# Input:A number (N) as an integer.
# 
# Output:The super root (x) as a float or an integer.
# 
# Precondition:
# 1 ≤ number ≤ 10 ** 10
# 
# 
# END_DESC

from sympy.solvers import solve
from sympy.abc import x

def super_root(number):
    score = solve(f'{number}-x**x', x)
    return float(score[0])