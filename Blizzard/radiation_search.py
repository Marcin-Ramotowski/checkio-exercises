#!/usr/bin/env checkio --domain=py run radiation-search

# The robots have learned that the last container which they picked up during a supply stop on another island is    radioactive.    There are five different kinds of spare parts contained within marked by number.    The radiation is emitted from the largest group of identical spare parts (where each part is adjacently joined).    Help them find this group and point out the quantity of identical parts within the group as well as    the number of the spare part itself in the container.
# 
# The container is represented as a square matrix.    The numbers 1 through 5 are used to label the different kinds of spare parts -- the elements of the matrix.    Zero is an empty cell.    Find the largest group of identical numbers adjacently joined to each other and    point out both the quantity of the spare parts within the group and the number of the spare part itself.
# 
# Input:A square matrix as a list of lists. Each list contains integers
# 
# Output:The size and marking of the largest group as a list of two integers.
# 
# Precondition:
# 3 ≤ len(matrix) ≤ 10
# all(all(0 ≤ x ≤ 5 for x in row) for row in matrix
# any(any(x for x in row) for row in matrix
# The tests have only one unique solutions.
# 
# 
# END_DESC

from itertools import chain
import numpy as np

def checkio(matrix):
    MOVES = ([1, 0],  [-1, 0], [0, 1], [0, -1])
    numbers = sorted(set(chain.from_iterable(matrix)))
    M = np.array(matrix)
    groups = []
    for n in numbers:
        positions = np.where(M == n)
        positions = list(zip(positions[0], positions[1]))
        queue = [positions.pop(0)]
        visited = set()
        Maxgroup, group = 0, 0
        while queue:
            place = queue.pop(0)
            if place in visited:
                continue
            x, y = place
            neighbours = [(x+X, y+Y)
                          for X, Y in MOVES if (x+X, y+Y) in positions]
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
                    positions.remove(neighbour)
            visited.add(place)
            group += 1
            if not(queue):
                if group > M.size//2:
                    return [group, n]
                Maxgroup = max(Maxgroup, group)
                group = 0
                if positions:
                    queue.append(positions.pop(0))
                else:
                    break
        groups.append((Maxgroup, n))
    return list(max(groups))