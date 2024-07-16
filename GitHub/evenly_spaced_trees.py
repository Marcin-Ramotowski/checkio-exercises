#!/usr/bin/env checkio --domain=py run evenly-spaced-trees

# You need to add some trees and keep them evenly spaced.
# 
# You are given a list of integers as an input value.This is the position of an existing tree.You must return the minimum number of additional trees needed so that they could be evenly spaced.
# 
# Positions of the existing trees are already sorted.All positions of trees are integers.Input:The position of the existing trees (a list of integers).
# 
# Output:The minimum number of additional trees (an integer).
# 
# How it is used:
# Landscape design.
# 
# Precondition:
# 0 ≤ Position of tree ≤ 1003 ≤ The existing trees
# 
# 
# END_DESC

from typing import List
from math import gcd


def evenly_spaced_trees(trees: List[int]) -> int:
    f, l = trees[0], trees[-1]
    diffes = [trees[i] - trees[i-1] for i in range(1, len(trees))]
    step = gcd(*diffes)
    return (l-f)//step-len(trees)+1