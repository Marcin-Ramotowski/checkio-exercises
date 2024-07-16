#!/usr/bin/env checkio --domain=py run permutation-index

# The mission is anideaofprzemyslaw.daniel.
# 
# Let’s imagine a list of all the permutations of a given set.    Every item on the list has it’s index (starting from 1).    The task is to calculate the permutation index.
# 
# You are given a tuple of integers.    It represents one of the permutations of the consecutive integers (starting from 0).    You have to return the permutation index of the tuple.
# 
# For example
# 
# Input: (1, 2, 0)All the consecutive permutations are:(0, 1, 2)(0, 2, 1)(1, 0, 2)(1, 2, 0) !!!(2, 0, 1)(2, 1, 0)Output: 4Input:One of the permutations of the consecutive integers (a tuple of integers).
# 
# Output:The permutation index (an integer).
# 
# Precondition:
# 
# sorted(input) == list(range(len(input)))
# END_DESC

from typing import Tuple
import math

def permutation_index(numbers: Tuple[int])->int:
    numbers2 = list(numbers)
    numbers2.sort()
    x,y = 1,0
    for number in numbers:
        index = numbers2.index(number)
        poss = index * math.factorial(len(numbers[y+1:]))
        numbers2.remove(number)
        x += poss
        y += 1
    return x