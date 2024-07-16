#!/usr/bin/env checkio --domain=py run strange-curcuit

# Nikola picks up a strange circuit board.    All of its elements are connected in a spiral and    it is possible to connect the neighboring elements vertically and horizontally.
# 
# The map of the circuit consists of a series of square cells. The first element in the center is marked as 1, and    continuing in a clockwise spiral, each other elements is marked in ascending order.    On the map, you can move (connect cells) vertically and horizontally.    You can help Nikola find the manhattan distance between any two elements on the map.    For example, the distance between cells 1 and 9 is two moves and the distance between 24 and 9 is one move.
# 
# 
# END_DESC

from math import sqrt
from numpy import zeros
from itertools import cycle

def generate_matrix(number):
    n = sqrt(number)
    n = int(n) + 1 if int(n) == n else int(n) + 2
    M = zeros((n,n),int)
    actions = cycle(['left','up', 'right', 'down'])
    vectors = [(0,-1), (-1,0), (0,1), (1,0)]
    lexicon = dict(zip(actions,vectors))
    k, l = 1, 2
    x = y = n//2
    M[x, y] = 1
    while l <= number:
            for j in range(2):
                action = next(actions)
                vector = lexicon[action]
                x2, y2 = vector
                for z in range(k):
                    if l > number:
                        break
                    x += x2
                    y += y2
                    M[x,y] = l
                    l += 1
            k += 1
    return M

def find_distance(c1,c2):
    maxNumber = max([c1,c2])
    M = generate_matrix(maxNumber)
    size = M.shape[0]
    coords = [(x,y) for x in range(size) for y in range(size) if M[x,y]==c1][0]
    coords2 = [(x,y) for x in range(size) for y in range(size) if M[x,y]==c2][0]
    scores = (abs(coords[0]-coords2[0]), abs(coords[1]-coords2[1]))
    return sum(scores)