#!/usr/bin/env checkio --domain=py run similar-triangles

# This is a mission to check thesimilarityof two triangles.
# 
# You are given two lists as coordinates of vertices of each triangle.
# You have to return a bool. (The triangles are similar or not)
# 
# Input:Two lists as coordinates of vertices of each triangle.Coordinates is three tuples of two integers.
# 
# Output:True or False.
# 
# Precondition:
# -10 ≤ x(, y) coordinate ≤ 10
# 
# 
# END_DESC

from typing import List, Tuple
from math import dist,acos,degrees

Coords = List[Tuple[int, int]]

def similar_triangles(first: Coords, second: Coords) -> bool:
    first.sort()
    second.sort()
    A,B,C = first
    A2,B2,C2 = second
    lengths1 = sorted([dist(A,B),dist(B,C),dist(A,C)])
    lengths2 = sorted([dist(A2,B2),dist(B2,C2),dist(A2,C2)])
    if lengths1 == lengths2: return True
    unique1, unique2 = set(lengths1), set(lengths2)
    if len(unique1) == 1 and len(unique2) == 1:
        return True  
    relations = [round(lengths1[0]/lengths2[0],2), round(lengths1[1]/lengths2[1],2), round(lengths1[2]/lengths2[2],2)]
    if len(set(relations)) == 1:
        return True
    
    angles1 = angles(lengths1)
    angles2 = angles(lengths2)
    if angles1 == angles2:
        return True
    if len(set(relations)) == 2:
        repeats = [i for i, value in enumerate(relations) if relations.count(value) == 2]
        hints = ([1,2],[0,2],[0,1])
        index = hints.index(repeats)
        if angles1[index] == angles2[index]:
            return True
    return False

def angles(sides:list):
    a, b, c = sides
    cosc = (a**2 + b**2 - c**2) / (2*a*b)
    cosb = (a**2 + c**2 - b**2) / (2*a*c)
    cosa = (b**2 + c**2 - a**2) / (2*b*c)
    cosinuses = [cosa, cosb, cosc]
    angles = [acos(cos) for cos in cosinuses]
    angles = list(map(degrees, angles))
    return list(map(lambda x:round(x,2),angles))