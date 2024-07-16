#!/usr/bin/env checkio --domain=py run shoot-range

# On a shooting range, shooters use a wall to practice, trying to hit it from various positions.    Shooters do not have problems with vertical deviation,    so we can use a simplified model for this mission.    We placed a camera above the shooting range and    useCartesian coordinatesto describe states.    We know coordinates of wall (target) ends and shooting point.    And we know the point where a bullet is after a small time.    You should determine the result of the shot.
# 
# You are given coordinates for the end-points of the target wall on a grid.    In addition, you have two points describing the shot: A starting point where the bullet was fired,    and a second point indicating the location of the bullet after a specified length of time.    You should calculate the result of the shot, specifically if a bullet hit the wall in the center,    then it's 100 points. Awarded points reduce in relation to the distance from the center.    An impact on the end of the wall is 0 points and a missed shot deducts a point (-1).    The result should berounded to the nearest integer.
# 
# 
# 
# Input:Four arguments. Two wall ends, a firing point and a later point as tuples of two numbers.
# 
# Output:The results as an integer from -1 to 100.
# 
# Preconditions:
# all(all(0 < i < 100 for i in coor) for coor in args)
# wall1, wall2 and shot_point are not collinear.
# 
# 
# END_DESC

from math import dist

def shot(w1,w2,s1,s2):
    cpoint = ((w1[0]+w2[0])/2,(w1[1]+w2[1])/2)
    dist1 = dist(s1, cpoint)
    dist2 = dist(s2, cpoint)
    if dist2 > dist1: # if direction of shot is wrong
        return -1

    r1 = [w2[0]-w1[0], w1[1]-w2[1], w1[0]*w2[1]-w1[1]*w2[0]] # r = [A,B,C]
    r2 = [s2[0]-s1[0], s1[1]-s2[1], s1[0]*s2[1]-s1[1]*s2[0]]
    A1, B1, C1 = r1
    A2, B2, C2 = r2
    W = A1*B2-A2*B1

    if W != 0:
        Wx = C1*A2-C2*A1
        Wy = B1*C2-B2*C1
        spoint = (Wx/W, Wy/W)
        x, y = spoint
        length = dist(w1, w2)  # length of wall
        distance = dist(cpoint, spoint)  # distance from cpoint to spoint
        procents = round(distance / (length / 2) * 100, 0)
        points = 100 - procents
        return points if points >= 0 else -1
    else:
        return -1