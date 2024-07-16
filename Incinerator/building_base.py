#!/usr/bin/env checkio --domain=py run building-base

# pre.example {        border: 1px solid #aaa;        border-radius: 3px;        background: #eee;        margin-left: 20px;        padding: 5px;        overflow: auto;    }    p.indent {        margin-left: 20px;    }The singularity has happened, and we are being made to build the ideal robo-city for our    overlords. In this shining robotropolis, all buildings will be rectangular and all streets laid    along south-north and east-west lines in a glorious grid. Before we get started, we have to create a    class to represent the perfect building.
# 
# Because all the buildings in the city are rectangular and their walls are parallel to the    streets, we can define any building using only the coordinates of South-Western corner as two    arguments (the length of the west to east walls, and the length of the north to south wall)    along with the height of the building. These values are described as positive numbers using    conventional units.The origin point of our coordinate system lies in the South-West, as a result, the northern corner ends up having the greater coordinate value than the southern    corner. To complete this mission we need to use a couple of operations. See the class description    below.
# 
# classBuilding(south, west, width_WE, width_NS, height=10)
# 
# Returns a new Building instance with the South-West corner at [south,west]    coordinates,    the size iswidth_WEbywidth_NSand the height of the building isheight.    "height" is a positive number with a default value of 10.
# 
# 
# >>> Building(10, 10, 1, 2, 2)
# Building(10, 10, 1, 2, 2)
# >>> Building(0, 0, 10.5, 2.546)
# Building(0, 0, 10.5, 2.546, 10)
# 
# corners()
# 
# Returns a dictionary with the coordinates of the building corners. The dictionary has following    keys: "north-west", "north-east", "south-west", "south-east". The values are lists or tuples    with two numbers.
# 
# 
# >>> Building(1, 2, 2, 2).corners()
# {"north-west": [3, 2], "north-east": [3, 4], "south-west": [1, 2], "south-east": [1, 4]}
# 
# area()
# 
# Returns the area of the building.
# 
# 
# >>> Building(1, 2.5, 4.2, 1.25).area()
# 5.25
# 
# volume()
# 
# Returns the volume of the building.
# 
# 
# >>> Building(1, 2.5, 4.2, 1.25, 101).volume()
# 530.25
# 
# __repr__()
# 
# This is a string representation of the Building. This method is used for "print" or "str"    conversion. Returns the string in the following view:
# "Building({south}, {west}, {width_we}, {width_ns}, {height})"
# 
# 
# 
# >>> str(Building(0, 0, 10.5, 2.546))
# "Building(0, 0, 10.5, 2.546, 10)"
# 
# In this mission, all data will be correct and you don't need to implement value checking.
# 
# Input:Statements and expression with the Building class.
# 
# Output:The behaviour as described.
# 
# Precondition:All data are correct.
# 
# 
# END_DESC

class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10) -> None:
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height
        self.east = self.west + self.width_WE
        self.north = self.south + self.width_NS
    def corners(self):
        directs = ([self.north,self.west], [self.north,self.east], [self.south, self.west], [self.south, self.east])
        strings = ['north-west', 'north-east', 'south-west', 'south-east']
        return dict(zip(strings,directs))
    def area(self):
        return self.width_WE * self.width_NS
    def volume(self):
        return self.width_WE * self.width_NS * self.height
    def __repr__ (self):
        return f"Building({self.south}, {self.west}, {self.width_WE}, {self.width_NS}, {self.height})"