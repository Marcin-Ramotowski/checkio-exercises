#!/usr/bin/env checkio --domain=py run find-sequence

# “There’s nothing here...” sighed Nikola.
# 
# “You’re kidding right? All treasure is buried treasure! It wouldn’t be treasure otherwise!” SaidSofia. “Here, take these.” She produced three shovels from a backpack that seemed to appear out of thin air.
# 
# “Where did you get-”
# 
# “Don’t ask questions. Just dig!” She hopped on the shovel and began digging furiously.
# 
# CLUNK
# 
# “Hey we hit something.” Stephen exclaimed in surprise.
# 
# “It’s the treasure!” Sofia was jumping up and down in excitement.
# 
# The trio dug around the treasure chest and pulled it out of the hole and wiped the dirt off. Sofia tried grabbing        the lid but it was locked. Nikola studied the locking mechanism.
# 
# “I’ve seen this type of lock before. It’s pretty simple. We just need to check whether there is a sequence of 4        or more matching numbers and output a bool.”
# 
# “Easy enough. Let’s open this sucker up!” Sofia was shaking in excitement.
# 
# 
# 
# You are given a matrix of NxN (4≤N≤10).    You should check if there is a sequence of 4 or more matching digits.    The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).
# 
# Input:A matrix as a list of lists with integers.
# 
# Output:Whether or not a sequence exists as a boolean.
# 
# Precondition:
# 0 ≤ len(matrix) ≤ 10
# all(all(0 < x < 10 for x in row) for row in matrix)
# 
# 
# END_DESC

import numpy as np
from typing import List

def checker(seq):
    for el in seq:
        dimensions = np.shape(el)
        xMax, yMax = dimensions
        elements = [el[i,j] for i in range(xMax) for j in range(yMax)]
        wanted = 0
        x = 0
        for number in elements:
            if elements.count(number) > 3:
                if x == 0:
                    wanted = number
                    x += 1
                    continue
            if x > 0:
                if number == wanted:
                    x += 1
                else:
                    x = 0
            if x == 4:
                return True
    return False

def checkio(matrix: List[List[int]]) -> bool:
    matrix = np.matrix(matrix)
    diff = len(matrix) - 4
    rows = [matrix[i,:] for i in range(len(matrix))]
    columns = (matrix[:,i] for i in range(len(matrix)))
    bevels = [matrix.diagonal(i) for i in range(-diff,diff+1)]
    matrix2 = np.rot90(matrix)
    bevels += [matrix2.diagonal(i) for i in range(-diff,diff+1)]
    if not(checker(rows)):
        if not(checker(columns)):
            if not(checker(bevels)):
                return False
    return True