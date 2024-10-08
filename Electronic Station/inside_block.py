#!/usr/bin/env checkio --domain=py run inside-block

# When it comes to city planning it's important to understand the borders of various city structures.    Parks, lakes or living blocks can be represented as closed polygon and can be described using    cartesian coordinates on a map. We need a functionality to determine if a point (a building or a    tree) lies inside the structure.
# 
# For the purpose of this mission, a city structure may be considered a polygon represented as a    sequence of vertex coordinates on a plane or map. The vertices are connected sequentially with    the last vertex in the list connecting to the first. We are given the coordinates of the point    which we need to check. If the point of impact lies on the edge of the polygon then it should be    considered inside of it. For this mission, you need to determine whether the given point lies    inside the polygon.
# 
# 
# 
# For example, on the left image you see a polygon which is described by    ((2,1),(1,5),(5,7),(7,7),(7,2)) and the point at (2,7). The result is False.
# For the right image the point lies on the edge and gets counted as inside the polygon,    making the result True.
# 
# Input:Two arguments. Polygon coordinates as a tuple of tuples with two    integers each.    A checking point coordinates as a tuple of two integers.
# 
# Output:Whatever the point inside the polygon or not as a boolean.
# 
# Precondition:
# all(x ≥ 0 and y ≥ 0 for x, y in polygon)
# point[0] ≥ 0 and point[1] ≥ 0
# 
# 
# END_DESC

from typing import Tuple

def is_inside(polygon, point):

    def cross(p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        # horizontal line
        if y1 - y2 == 0:
            if y1 == point[1]:
                if min(x1, x2) <= point[0] <= max(x1, x2):
                    return 1, True
            return 0, False

        # vertical line
        if x1 - x2 == 0:
            if min(y1, y2) <= point[1] <= max(y1, y2):
                if point[0] <= max(x1, x2):
                    return 1, point[0] == max(x1, x2)
            return 0, False

        # diagonal line
        a = (y1 - y2) / (x1 - x2)
        b = y1 - x1 * a
        x = (point[1] - b) / a
        if point[0] <= x:
            if min(y1, y2) <= point[1] <= max(y1, y2):
                return 1, point[0] == x or point[1] in (y1, y2)
        return 0, False

    # MAIN
    cross_points = 0
    for x in range(len(polygon)):
        num, on_line = cross(polygon[x], polygon[x-1])
        if on_line:
            return True
        cross_points += num

    return cross_points % 2

if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) is True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) is False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) is True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)),
                     (3, 3)) is False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) is True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) is False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) is True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) is False, "Eighth"
    print("All done! Let's check now")