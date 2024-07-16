#!/usr/bin/env checkio --domain=py run triangle-angles

# You are given the lengths for each side on a triangle.    You need to find all three angles for this triangle.    If the given side lengths cannot form a triangle (or form a degenerated triangle),    then you must return all angles as 0 (zero).    The angles should be represented as a list of integers inascending order.    Each angle is measured in degrees and rounded to the nearest integer number (Standard mathematical rounding).
# 
# 
# 
# Input:The lengths of the sides of a triangle as integers.
# 
# Output:Angles of a triangle in degrees as sorted list of integers.
# 
# Precondition:
# 0 < a,b,c ≤ 1000
# 
# 
# END_DESC

from typing import List
import math


def checkio(a: int, b: int, c: int) -> List[int]:
    sides = [a, b, c]
    sides. sort()
    a, b, c = sides
    if c >= b + a:
        return [0, 0, 0]
    cosc = (a**2 + b**2 - c**2) / (2*a*b)
    cosb = (a**2 + c**2 - b**2) / (2*a*c)
    cosa = (b**2 + c**2 - a**2) / (2*b*c)
    cosinuses = [cosa, cosb, cosc]
    angles = [math.acos(cos) for cos in cosinuses]
    angles = map(math.degrees, angles)
    rounding = lambda number: int(number) if number - int(number) < 0.5 else int(number) + 1
    angles = map(rounding, angles)
    return list(angles)