#!/usr/bin/env checkio --domain=py run lightbulb-start-watching

# This is the second mission in the lightbulb series. I will try to make each following task slightly more complex.
# 
# You have already learned how to count the amount of time a light bulb has been on, or how long a room has been lit. Now let's add one more parameter - the counting start time.
# 
# This means that the light continues to turn on and off as before. But now, as a result of the function, I want not only to know how long there was light in the room, but how long the room was lit, starting from a certain moment.
# 
# One more argument is added –start_watching, and if it’s not passed, we count as in the previous version of the program for the entire period.
# 
# Input:Two arguments and only the first one is required. The first one is a list of datetime objects and the second one is a datetime object.
# 
# Output:A number of seconds as an integer.
# 
# Precondition:
# 
# The array of pressing the button is always sorted in ascending orderThe array of pressing the button has no repeated elementsThe amount of elements is always even (the light will eventually be off)The minimum possible date is 1970-01-01The maximum possible date is 9999-12-31
# END_DESC

from datetime import datetime
from typing import List, Optional

def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    if start_watching:
        times = [z for z in els if z >= start_watching]
        index = els.index(times[0])
        if index % 2 == 1:
            times = [start_watching] + times
        iters = [iter(times)] * 2
        pairs = list(zip(*iters))
        return sum([(pair[1] - pair[0]).total_seconds() for pair in pairs])
    else:
        iters = [iter(els)] * 2
        pairs = list(zip(*iters))
        return sum([(pair[1] - pair[0]).total_seconds() for pair in pairs])


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
    datetime(2015, 1, 12, 10, 0, 5)))
    
    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
    start_watching=datetime(2015, 1, 12, 10, 0, 5)) == 5
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ], datetime(2015, 1, 12, 10, 0, 0)) == 10
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 11, 0, 0)) == 610
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 11, 0, 10)) == 600
    
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 10, 10, 0)) == 620

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 11),
        datetime(2015, 1, 12, 12, 10, 11),
    ], datetime(2015, 1, 12, 12, 10, 11)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 11),
        datetime(2015, 1, 12, 12, 10, 11),
    ], datetime(2015, 1, 12, 12, 9, 11)) == 60
    
    print("The second mission in series is done? Click 'Check' to earn cool rewards!")