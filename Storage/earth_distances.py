#!/usr/bin/env checkio --domain=py run earth-distances

# To describe a specific position on the surface of the Earth, we must rely on thegeographic coordinate        system.    The geographic coordinate system is a method used to give every possible location on Earth to be    specified by a set of numbers or letters. A common choice of coordinates islatitudeandlongitude.    With this information we can calculate a distance between two points along a surface.
# 
# For simplicity’s sake, we will suppose that the Earth is a perfect sphere with a radius of 6,371    kilometers (it gives a mistake no more than 0.3%).    You are given two point coordinates and you must find the shortest distance between    these points on the surface of the Earth, measured along the surface of the Earth.
# 
# Coordinates are given as a string with the latitude and longitude separated by comma and/or whitespace.    Latitude and longitude are represented in the follow format:
# 
# 
#     d°m′s″X
# 
# In this example, "d" is degrees, "m" is minutes, "s" is seconds as integers, while "X" is "N"    (north) or "S" (south) for a latitude and "W" (west) or "E" (east) for a longitude.
# 
# The result should be given as a number in kilometers with a precision of ±0.1 (100 metres).
# 
# Input:Two arguments. Coordinates as strings (unicode).
# 
# Output:The distance as a number (int or float).
# 
# 
# 
# Precondition:Correct Coordinates.
# 
# 
# END_DESC

from math import pi, cos, asin, sqrt

R = 6371

def preparing(coords: str):
    coords = coords.split() if ',' not in coords else coords.split(',')
    chars = ["°", "′", "″"]
    positive = ['N', 'E']
    point = []
    for value in coords:
        whole = [value]
        for i in range(3):
            value = whole.pop(-1)
            whole.extend(value.split(chars[i]))
        X = whole[-1]
        numbers = list(
            map(int, whole[:-1])) if X in positive else [-int(item) for item in whole[:-1]]
        d, m, s = numbers
        score = d + m/60 + s/3600
        point.append(score)
    return point


def distance(point1, point2):
    point1, point2 = preparing(point1), preparing(point2)
    lat1, lon1 = point1
    lat2, lon2 = point2
    p = pi/180
    R = 6371
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * \
        cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    score = 2 * R * asin(sqrt(a))
    return round(score, 1)