#!/usr/bin/env checkio --domain=py run fast-train

# You are planning the train schedule and you want to know the minimum time of traveling between the stations.
# 
# Each section of the rail between stations is given in the list.Each section is a tuple of distance and speed limit (both are integers).You can change the speed ( +1. -1 and ± 0 ) at the start and every minute after that.The train runs by the same amount as the speed value in a minute.
# Note: This means that a train with a speed 2 will travel a distance 2 before another minute passes and its speed can be changed again.
# 
# Starting speed is 0.Speed limit is set for each section of the rail.        You don't exceed it.You must reach the target station at speed 1 (because it’s necessary to stop at the station).You should return the minimum time (minutes) as an integer.
# 
# 
# 
# Input:A list of the section of the rail. Each section is a tuple of distance (as an integer) and speed limit (as an integer).
# 
# Output:The minimum time (minutes) as an integer.
# 
# How it is used:
# For efficient acceleration and deceleration.
# 
# Precondition:
# distance > 0speed limit > 0len(section) > 0
# 
# 
# END_DESC

# Rozwiązanie gracza Phil15
def fast_train(sections): #BFS (Algorytm przeszukiwania grafu wszerz) tworzy najkrótszą listę prędkości
    limit = sum(([speed] * dist for dist, speed in sections), [])
    print(limit)
    q, end = [[1]], len(limit)
    while q: # kolejka możliwych list prędkości
        speeds = q.pop(0)
        pos, speed = sum(speeds), speeds[-1] # obecna pozycja/prędkość
        if pos == end and speed == 1: return len(speeds)
        q += [speeds + [s] for s in (speed + 1, speed, speed - 1)
              if 0 < s <= end - pos and all(s <= limit[pos + i] for i in range(s))]