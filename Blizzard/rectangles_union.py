#!/usr/bin/env checkio --domain=py run rectangles-union

# Your mission is to calculate the area covered by a union of rectangles. The rectangles can have a non-empty intersection, which means that a simple sum of given rectangle areas doesn't work. Every rectangle is represented as 4 integers. The first two integers are the coordinates of a left-top corner, and the next two - of a bottom right corner.
# 
# 
# 
# 
# 
# Input:Iterable with tuples.
# 
# Output:Int.
# 
# 
# END_DESC

from itertools import chain
from numpy import zeros

def rectangles_union(rectangles):
    if len(rectangles) == 0:
        return 0
    numbers = list(chain.from_iterable(rectangles)) # all numbers in rectangles
    Min = min(numbers)
    Max = max(numbers)
    if Min < 0: # if sequence have negative numbers
        Min = -Min
        Max = max(numbers) + Min
        rectangles = list(map(list, rectangles))
        for i, rec in enumerate(rectangles):
            for j,number in enumerate(rec):
                rectangles[i][j] += Min
    M = zeros((Max,Max))
    for r in rectangles:
        xMin, yMin, xMax, yMax = r
        for i in range(xMin,xMax):
            for j in range(yMin,yMax):
                M[i,j] = 1 # number of ones = area of figures
    return len(M[M==1])