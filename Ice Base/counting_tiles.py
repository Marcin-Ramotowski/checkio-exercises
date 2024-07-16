#!/usr/bin/env checkio --domain=py run counting-tiles

# Stephan needs some help building a circular landing zone using the ice square tiles for their new Ice Base.    Before he converts the area to a construction place, Stephan needs to figure out how many square tiles he will need.
# 
# Each square tile has size of 1x1 meters.     You need to calculate how many whole and partial tiles are needed for a circle with a radius of N meters.     The center of the circle will be at the intersection of four tiles. For example: a circle with a radius of 2 metres    requires 4 whole tiles and 12 partial tiles.
# 
# Input:The radius of a circle as a float
# 
# Output:The quantities whole and partial tiles as a list with two integers -- [solid, partial].
# 
# Precondition:
# 0 < radius ≤ 4
# 
# 
# 
# 
# 
# 
# 
# END_DESC

from math import sqrt

def checkio(R):
    whole = 0
    partial = 0
    intR = int(R)
    diffR = R - intR
    if diffR != 0:
        x = intR + 1
    else:
        x = intR
    numbers = [i for i in range(-x, x)]
    for row in numbers:
        for column in numbers:
            i = 0
            point1 = (row, column)
            point2 = (row, column + 1)
            point3 = (row + 1, column + 1)
            point4 = (row + 1, column)
            points = [point1, point2, point3, point4]
            for point in points:
                x, y = point
                diff = sqrt(x ** 2 + y ** 2)
                if diff <= R:
                    i += 1
            if i == 4:
                whole += 1
            elif i > 0:
                partial += 1
    return [whole, partial]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"