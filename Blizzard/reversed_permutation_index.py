#!/usr/bin/env checkio --domain=py run reversed-permutation-index

# This mission is the inverse function ofPermutation Index.    (The mission idea is byprzemyslaw.daniel.)
# 
# You are given the length of the permutation (an integer) and the permutation index (an integer starting from 1).    The task is to calculate one of the permutations of the consecutive integers (starting from 0) and return it    (an iterable of integers).
# 
# For example
# 
# Input: 3, 4All consecutive permutations are:(0, 1, 2)(0, 2, 1)(1, 0, 2)(1, 2, 0) !!!(2, 0, 1)(2, 1, 0)Output: (1, 2, 0)Input:The length of the permutation (an integer) and the permutation index (an integer).
# 
# Output:One of the permutations (an iterable of integers).
# 
# Precondition:
# 
# 1 ≤ length1 ≤ permutation_index ≤ math.factorial(length)
# END_DESC

from typing import Iterable
import math


def reversed_permutation_index(length: int, index: int) -> Iterable[int]:
    numbers = list(range(length))
    perm = []
    index -= 1
    for i in range(length):
        f = math.factorial(length - i - 1)
        q = index // f
        perm.append(numbers[q])
        numbers.remove(numbers[q])
        index -= f * q
    return perm