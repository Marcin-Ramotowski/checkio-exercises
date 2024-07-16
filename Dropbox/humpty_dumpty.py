#!/usr/bin/env checkio --domain=py run humpty-dumpty

# .story.shadow {        float: left;        /*padding: 10px;*/        margin: 10px;        border: black;    }After reading this fragment Nicola wants to build his own "Humpty Dumpty".    As a basis he chooses the spheroid (read more about it on Wikipedia).    We know the height and the width (in inches) for this spheroid. For the job at hand, Nikola needs to know how much material is required.
# 
# You can help him and create a function to calculate the volume (cubic inches) and the surface area (square    inches).
# 
# 
# 
# Tips:Be careful withsin-1x-- this isarcsin.
# 
# Input:Two arguments. A height and a width as integers.
# 
# Output:The volume and the surface area as a list of floats. The results should be accurate to two    decimals.
# 
# Precondition:0 < width < 100
# 0 < height < 100
# 
# 
# 
# END_DESC

def checkio(height, width):
    return [1, 1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"