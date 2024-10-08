#!/usr/bin/env checkio --domain=py run buildings-visibility

# For ourfuture    Robotropoliswe need to help the city planners calculate the way light reaches our fair city    so as to limit the Urban Canyon effect. To do this, you will need to define the visibility of    buildings from the southern edge of the base. You have been given a map of the buildings in the    complex as an aide for your planning.
# 
# The map is an orthogonal projection of each of the buildings onto a horizontal plane. It’s    oriented on a rectangular coordinate system so that the positive x-axis points east and the    positive y-axis points north. No two buildings in the map overlap or touch. Each of the    buildings have perfectly rectangular sides which are aligned from north to south and east to    west. The map is a list of buildings with each building presented as a list with coordinates    describing the south-west corner, and north-east corner along with the height - [Xsw, Ysw, Xne,    Yne, height]. We need to determinate how many of the buildings are visible from the area just    south of the base (excluding the angle of vision, just using projection.) See the illustration    below.
# 
# Input:Building coordinates and heights as a list of lists.    The coordinates are integers. The heights are integers or floats.
# 
# Output:The quantity of visible buildings as an integer.
# 
# Precondition:
# 0 < len(buildings) < 10
# all(all(0 ≤ x < 12 for x in row[:4]) for row in buildings)
# all(0 < row[4] ≤ 20 for row in buildings)
# 
# 
# 
# END_DESC

def merge_intervals(intervals):
    if not intervals: return []
    intervals = sorted(intervals)
    L, H = intervals[0]
    for l, h in intervals[1:]:
        if l <= H: H = max(H, h)
        else: yield L, H; L, H = l, h
    yield L, H


def checkio(buildings):
    buildings = sorted(buildings, key= lambda y: y[1])
    intervals = []
    visible = len(buildings)

    for build in buildings:
        xMin, yMin, xMax, yMax, h = build
        covered = []
        for items in intervals:
            xMin2, xMax2, h2 = items
            if h2 >= h:
                if xMin2 <= xMin <= xMax <= xMax2: # przesłonięte
                    covered.append([xMin,xMax])
                    break
                elif xMin <= xMin2 <= xMax2 <= xMax:
                    covered.append([xMin2,xMax2])
                elif xMin <= xMin2 <= xMax <= xMax2:
                    covered.append([xMin2,xMax])
                elif xMin2 <= xMin <= xMax2 <= xMax:
                    covered.append([xMin, xMax2])
        if covered:
            numbers = list(merge_intervals(covered))
            if numbers == [(xMin,xMax)]:
                visible -= 1
        intervals.append([xMin,xMax,h])
    return visible


if __name__ == '__main__':
    assert checkio([
        [1, 1, 4, 5, 3.5],
        [2, 6, 4, 8, 5],
        [5, 1, 9, 3, 6],
        [5, 5, 6, 6, 8],
        [7, 4, 10, 6, 4],
        [5, 7, 10, 8, 3]
    ]) == 5, "First"
    assert checkio([
        [1, 1, 11, 2, 2],
        [2, 3, 10, 4, 1],
        [3, 5, 9, 6, 3],
        [4, 7, 8, 8, 2]
    ]) == 2, "Second"
    assert checkio([
        [1, 1, 3, 3, 6],
        [5, 1, 7, 3, 6],
        [9, 1, 11, 3, 6],
        [1, 4, 3, 6, 6],
        [5, 4, 7, 6, 6],
        [9, 4, 11, 6, 6],
        [1, 7, 11, 8, 3.25]
    ]) == 4, "Third"
    assert checkio([
        [0, 0, 1, 1, 10]
    ]) == 1, "Alone"
    assert checkio([
        [2, 2, 3, 3, 4],
        [2, 5, 3, 6, 4]
    ]) == 1, "Shadow"