#!/usr/bin/env checkio --domain=py run robot-sort

# The spaceship reactors contains several (no more than ten) nuclear fuel rods.    These rods should be sorted by size to ensure the reactor’s stability,    but as usual the fuel rod loading mechanism malfunctioned and inserted the rods at random,    then started the ships engine. Now Stephan has to reload the rods all over again.    Because the reactor is already running, he needs to quickly swap neighbouring rods or else the whole thing goes BOOM!
# 
# You are given the sizes and initial order of the rods as an array of numbers. Indexes are position, values are sizes.    You should order this array from the smallest to the largest in size.
# 
# For each action Stephan can swap only two neighbouring elements.    Each action should be represented as a string with two digits - indexes of the swapped elements    (ex, "01" - swap 0th and 1st rods).    The result should be represented as a string that contains the sequence of actions separated by commas.    If the array does not require sorting, then return an empty string.
# 
# And you can swap onlyN*(N-1)/2times, where N - is a quantity of rods.
# 
# 
# 
# Input:An array as a tuple of integers.
# 
# Output:The sequence of actions as a string.
# 
# Precondition:
# 1 ≤ len(array) ≤ 10
# all(1 ≤ n < 10 for n inarray)
# 
# 
# END_DESC

def swapsort(array):
    array = list(array)
    score = sorted(array)
    comments = []
    while array != score:
        for i in range(1,len(array)):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                comments.append(f"{i-1}{i}")
    return ','.join(comments)