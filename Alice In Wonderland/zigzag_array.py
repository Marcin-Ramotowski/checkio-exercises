#!/usr/bin/env checkio --domain=py run zigzag-array

# This function creates an List of lists. that represents a two-dimensional grid with the given number of rows and  cols. This grid should contain the integers fromstarttostart + rows * cols - 1in ascending order, but the elements of every odd-numbered row have to be listed in descending order, so that when read in ascending order, the numbers zigzag through the two-dimensional grid.
# 
# Input:Two ints rows and cols. One optional argument start.
# 
# Output:List of lists.
# 
# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

from typing import List
from numpy import zeros

def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:
    zigzag = zeros((rows,cols),int)
    numbers = iter(range(start,rows*cols+start))
    for i in range(rows):
        if i % 2 == 0:
            for j in range(cols):
                zigzag[i,j] = next(numbers)
        else:
            for j in range(cols-1,-1,-1):
                zigzag[i,j] = next(numbers)
    return [list(zigzag[i,:]) for i in range(rows)]