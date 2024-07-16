#!/usr/bin/env checkio --domain=py run matrix-pattern

# To explore new islands and areas Sophia uses automated drones. But she gets tired looking at the monitors all the time.    Sophia wants to teach the drones to recognize some basic patterns and mark them for review.
# 
# The drones have a simple optical monochromatic image capturing system.    With it an image can be represented as a binary matrix.    You should write a program to search a binary matrix (a pattern) within another binary matrix (an image).    The recognition process consists of scanning the image matrix row by row (horizontal scanning) and    when a pattern is located on the image, the program must mark this pattern. To mark a located pattern change 1 to 3 and 0 to 2.    The result will be the image matrix with the located patterns marked.
# 
# The patterns in the image matrix are not crossed, because you should immediately mark the pattern.
# 
# 
# 
# Input:Two arguments. A pattern as a list of lists and an image as a list of lists.
# 
# Output:The marked image as a matrix as a list of list.
# 
# Precondition:
# 1 < image_width ≤ 10
# 1 < image_height ≤ 10
# 1 < pattern_width ≤ 10
# 1 < pattern_height ≤ 10
# |pattern| < |image|
# ∀ x ∈ data : x == 0 or x == 1
# 
# 
# 
# END_DESC

def checkio(pattern, image):
    for i in range(len(image) - len(pattern)+1):
        row = image[i]
        for j in range(len(row)):
            isMatched = True
            x = len(pattern[0])
            indexes = []
            for k in range(len(pattern)):
                part = image[i+k][j:j+x]
                indexes += [(i+k, n) for n in range(j, j + x)]
                if part != pattern[k]:
                    isMatched = False
                    break
            if isMatched:
                for x, y in indexes:
                    image[x][y] += 2
    return image