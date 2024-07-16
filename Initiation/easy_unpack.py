#!/usr/bin/env checkio --domain=py run easy-unpack

# Your mission here is to create a function that gets a tuple and returns a tuple with 3 elements - the first, third and second element from the last for the given array.
# 
# 
# 
# One important thing worth pointing out is that you need to use index in order to extract elements from the array. Pay attention, index counting starts from 0, not from 1. Which means that if you need to get the first element from the arrayelements, you should doelements[0], and the second element iselements[1].
# 
# Input:A tuple, at least 3 elements long.
# 
# Output:A tuple.
# 
# 
# END_DESC

def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    return elements[0], elements[2], elements[-2]