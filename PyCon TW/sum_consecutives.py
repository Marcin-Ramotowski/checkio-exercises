#!/usr/bin/env checkio --domain=py run sum-consecutives

# You are given a list that contains solely integers (positive and negative). Your job is to sum only the numbers that are identical and consecutive.
# 
# Input:a list.
# 
# Output:an iterable.
# 
# 
# END_DESC

def sum_consecutives(data):
    if len(data) < 2:
        return data
    data.append('0')
    scores = []
    wanted = None
    for i in range(len(data)):
        if wanted == None:
            wanted = data[i]
            score = wanted
        elif data[i] == wanted:
            score += wanted
        elif data[i] != wanted:
            wanted = data[i]
            scores.append(score)
            score = wanted
    return scores