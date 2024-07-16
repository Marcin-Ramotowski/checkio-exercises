#!/usr/bin/env checkio --domain=py run simple-areas

# Stephan works with simple forms when constructing something,    and he need some programming tools to calculate his expenses.    Let's take a trip back to our school days and pull out some simple geometry for this.
# 
# You should write a function to calculate the area of simple figures: circles, rectangles and triangles.    You are give an arbitrary number of arguments and depending on this,    the function calculates area for the different figures.
# 
# One argument -- The diameter of a circle and you need calculate the area of the circle.Two arguments -- The side lengths of a rectangle and you need calculate the area of the rectangle.Three arguments -- The lengths of each side on a triangle and you need calculate the area of the triangle.
# 
# The result should be given with two digits precision as ±0.01.
# 
# Tips:Think about how to work withan arbitrary number of        arguments.
# 
# Input:One, two or three arguments as floats or as integers.
# 
# Output:The area of the circle, the rectangle or the triangle as a float.
# 
# Precondition:
# 0 < len(args) ≤ 3
# all(0 < x ≤ 1000 for x in args)
# For "triangle" cases the sum of the lengths of any two sides always exceeds the length of the third side.
# 
# 
# END_DESC

from math import sqrt, pi

def simple_areas(*args):
    l = len(args)
    if l < 3:
        return pi*(args[0]/2)**2 if l==1 else args[0]*args[1]
    else:
        a,b,c = args
        p = sum([a,b,c])/2
        return sqrt(p*(p-a)*(p-b)*(p-c))