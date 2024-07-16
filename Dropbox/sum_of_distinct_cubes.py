#!/usr/bin/env checkio --domain=py run sum-of-distinct-cubes

# Positive integers can be broken down into sums of distinct cubes of positive integers, sometimes in multiple different ways. Your function should find and return the descending list of distinct cubes whose sum equals the given positive integern. If it is impossible to expressnas a sum of distinct cubes, returnNone.
# 
# Ifnallows several breakdowns into sums of distinct cubes, the function must return the lexicographically highest solution that starts with the largest possible first number, followed by the lexicographically highest representation of the rest of the numbern-a*a*a. For example, called withn = 1729, this  function should return[12, 1]instead of[10, 9].
# 
# Input:Positive integer(int).
# 
# Output:Listof integers(int)orNone.
# 
# Examples:
# 
# assert sum_of_cubes(1729) == [12, 1]
# assert sum_of_cubes(8) == [2]
# assert sum_of_cubes(11) == None
# Precondition:n > 0.
# 
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def sum_of_cubes(n: int) -> list[int] | None:
    # your code here
    return []


print("Example:")
print(sum_of_cubes(1729))

# These "asserts" are used for self-checking
assert sum_of_cubes(1729) == [12, 1]
assert sum_of_cubes(8) == [2]
assert sum_of_cubes(11) == None

print("The mission is done! Click 'Check Solution' to earn rewards!")