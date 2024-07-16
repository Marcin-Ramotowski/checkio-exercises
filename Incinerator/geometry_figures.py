#!/usr/bin/env checkio --domain=py run geometry-figures

# You often work with the different geometrical figures and with their parameters - the perimeter, area, and volume. You are tired of doing it manually, so you’ve decided to automate this process, and therefore you need to write a particular program. In this program you should create the class Parameters which will choose one of the few figures (the circle, regular triangle, square, regular pentagon, regular hexagon, cube) using thechoose_figure()method and will count the perimeter, area, and volume with the help of the following methods:
# 
# perimeter()- returns the perimeter of the figure;
# area()- returns the area of the figure;
# volume()- returns the volume of the figure.
# 
# Also you have to create a class for each figure and use theStrategydesign pattern to solve this mission.
# Every figure, except the cube, has the volume = 0.
# If the result has no decimal places, you should return it as int(), in other case - round it to the 2 decimal points.
# 
# Examples:
# figure = Parameters(10)
#     
# figure.choose_figure(Circle())
# figure.area() == 314.16
# 
# figure.choose_figure(Triangle())
# figure.perimeter() == 30
# 
# figure.choose_figure(Square())
# figure.area() == 100
# 
# figure.choose_figure(Pentagon())
# figure.perimeter() == 50
# 
# figure.choose_figure(Hexagon())
# figure.perimeter() == 60
# 
# figure.choose_figure(Cube())
# figure.volume() == 1000
# 
# 
# 
# Input:Statements and expressions of the classes.
# 
# Output:The perimeter, area, and volume (number).
# 
# Precondition:All data is correct.
# 
# 
# END_DESC

from abc import ABC
from math import pi, sqrt

class Figure(ABC):
    def __init__(self, a=0) -> None:
        self.a = a
    def volume(self):
        return 0
    def rounding(self, x):
        return int(x) if int(x) == x else round(x,2)

class Circle(Figure):
    def perimeter(self):
        return self.rounding(2 * pi * self.a)

    def area(self):
        return self.rounding(pi * self.a**2)

class Triangle(Figure):
    ''' regular triangle '''
    def perimeter(self):
        return self.rounding(3 * self.a)
    
    def area(self):
        return self.rounding((self.a**2 * sqrt(3)) / 4)

class Square(Figure):
    def perimeter(self):
        return self.rounding(4 * self.a)

    def area(self):
        return self.rounding(self.a**2)

class Pentagon(Figure):
    ''' regular pentagon '''
    def perimeter(self):
        return self.rounding(5 * self.a)
    
    def area(self):
        return self.rounding(sqrt(25+10*sqrt(5))/4 * self.a**2)
    
class Hexagon(Figure):
    '''regular hexagon '''
    def perimeter(self):
        return self.rounding(6 * self.a)
    
    def area(self):
        return self.rounding(6*(self.a**2 * sqrt(3) / 4))

class Cube(Figure):
    def perimeter(self):
        return self.rounding(12 * self.a)
    
    def area(self):
        return self.rounding(6 * self.a**2)
    
    def volume(self):
        return self.rounding(self.a**3)

class Parameters():
    def __init__(self, a) -> None:
        self.a = a
        self.figure = None
    
    def choose_figure(self, figure: object) -> None:
        figure.a = self.a
        self.figure = figure
    
    def perimeter(self):
        return self.figure.perimeter()
    
    def area(self):
        return self.figure.area()
    
    def volume(self):
        return self.figure.volume()