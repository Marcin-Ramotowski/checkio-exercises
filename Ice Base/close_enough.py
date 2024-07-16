#!/usr/bin/env checkio --domain=py run close-enough

# Except when the prime factors ofa, balready co-operate, the iron hand of theFundamental Theorem of Arithmeticdictates that the integer powersa**paandb**pbcan never be equal for any two positive integer exponentspaandpb. However, in the jovial spirit of“close enough for government work”, we define two such powers to “hit” if their differenceabs(a**pa-b**pb)multiplied by thetoleranceis at most equal to the smaller of those powers. (This definition intentionally avoids division to keep it both fast and accurate for arbitrarily large integers.) For example,tolerance=100expectsa**paandb**pbto be within 1 %.
# 
# For given positive integersa, breturn the smallest positive integer exponents(pa, pb)that satisfy thetolerancerequirement.
# 
# Input:Three integers(int).
# 
# Output:Tuple(or list) of two integers(int).
# 
# Examples:
# 
# assert list(hitting_powers(9, 10, 5)) == [1, 1]
# assert list(hitting_powers(2, 4, 100)) == [2, 1]
# assert list(hitting_powers(2, 7, 100)) == [73, 26]
# assert list(hitting_powers(3, 6, 100)) == [137, 84]
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def hitting_powers(a: int, b: int, tol: int = 100) -> tuple[int, int] | list[int]:
    # your code here
    return ()


print("Example:")
print(hitting_powers(9, 10, 5))

# These "asserts" are used for self-checking
assert list(hitting_powers(9, 10, 5)) == [1, 1]
assert list(hitting_powers(2, 4, 100)) == [2, 1]
assert list(hitting_powers(2, 7, 100)) == [73, 26]
assert list(hitting_powers(3, 6, 100)) == [137, 84]

print("The mission is done! Click 'Check Solution' to earn rewards!")