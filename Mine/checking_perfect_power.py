#!/usr/bin/env checkio --domain=py run checking-perfect-power

# A positive integernis aperfect powerif it can be expressed as the powerbefor some two integersbandethat are both greater than one. (Any positive integer n can always be expressed as the trivial power n1, so we don’t care about those.) For example, the integers 32, 125 and 441 are perfect powers since they equal 25, 53and 212, respectively.
# 
# This function should determine whether the positive integernis a perfect power. Your function needs to somehow iterate through a sufficient number of possible combinations ofbandethat could work, returningTrueright away when you find somebandethat satisfybe== n, and returningFalsewhen all relevant possibilities forbandehave been tried and found wanting.
# 
# Sincencan get pretty large, your function should not examine too many combinations above and beyond those that are both necessary and sufficient to reliably determine the answer. Achieving this efficiency is the central educational point of this problem.
# 
# Input:Integer(int).
# 
# Output:Logic value(bool).
# 
# Examples:
# 
# assert perfect_power(8) == True
# assert perfect_power(42) == False
# assert perfect_power(441) == True
# assert perfect_power(469097433) == True
# Preconditions:n > 0.
# 
# Related to the mission, you may be interested atCatalan’s conjecture, these days a proven mathematical theorem that says that after the special case of the two consecutive perfect powers 8 and 9, whenever a positive integernis a perfect power,n – 1is never a perfect power. For example, we don’t have to slog through all potential ways to express the number as an integer power to know from the get-go that 1234567890-1 is not a perfect power. This also illustrates the common asymmetry between performing a computation to opposite directions. Given some big chungus integer such as 4922235242952026704037113243122008064, but not the formula that originally produced it, it is not quite easy to tell whether that integer is a perfect power, or some perfect power plus minus one.
# 
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def perfect_power(n: int) -> bool:
    # your code here
    return False


print("Example:")
print(perfect_power(9))

# These "asserts" are used for self-checking
assert perfect_power(8) == True
assert perfect_power(42) == False
assert perfect_power(441) == True
assert perfect_power(469097433) == True
assert perfect_power(4922235242952026704037113243122008064) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")