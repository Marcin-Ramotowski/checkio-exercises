#!/usr/bin/env checkio --domain=py run stair-steps

# There is a staircase with N steps and two platforms; one at the beginning, the other at the end of the stairs.     On each step a number is written (ranging from -100 to 100 with the exception of 0.)    Zeros are written on both platforms.    You start going up the stairs from the first platform, to reach the top on the second one.    You can move either to the next step or to the next step plus one.    You must find the best path to maximize the sum of numbers on the stairs on your way up and return the final sum.
# 
# 
# 
# Input:Numbers on each stair as a list of integers.
# 
# Output:The final sum for the best way as an integer.
# 
# Precondition:
# 0 < len(steps) ≤ 10
# all(-100 < x < 100 and x for x in steps)
# 
# 
# END_DESC

def checkio(stairs) -> int:
    l = len(stairs)
    stairs[1] += max(0, stairs[0])
    for i in range(2, l):
        stairs[i] += max(stairs[i-1], stairs[i-2])
    return max(stairs[-1], stairs[-2])