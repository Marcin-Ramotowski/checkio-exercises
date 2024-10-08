#!/usr/bin/env checkio --domain=py run group-equal-consecutive

# Given a list of elements, create and return a list whose elements are lists that contain the consecutive runs of equal elements of the original list. Note that elements that aren’t duplicated in the original list should become singleton lists in the result, so that every element gets included in the resulting list of lists.
# 
# Input:List of str and int.
# 
# Output:List of lists of str and int
# 
# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def group_equal(data:list):
    if not(data): return data
    wanted = None
    data.append(None)
    score = []
    underscore = []
    for item in data:
        if item == wanted:
            underscore.append(item)
        else:
            wanted = item
            if underscore: score.append(underscore)
            underscore = [wanted]
    return score