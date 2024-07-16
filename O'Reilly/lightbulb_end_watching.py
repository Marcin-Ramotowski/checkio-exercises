#!/usr/bin/env checkio --domain=py run lightbulb-end-watching

# In the third mission from the series about lightbulbs, I want to separately highlight the process and the period of observation of this process.
# 
# In the previous mission, the start_watching parameter was introduced, and in this one - the end_watching parameter, which tells the time when it’s necessary to end the observation. If it’s not passed, the mission works as in the previous version, with no observation time limit.
# 
# One more update is that the amount of elements (button clicks) can be odd (previously there was a precondition, that the amount of elements is always even).
# 
# Input:Three arguments and only the first one is required. The first one is a list of datetime objects, the second and the third ones are the datetime objects.
# 
# Output:A number of seconds as an integer.
# 
# Precondition:
# 
# The array of pressing the button is always sorted in ascending order.The array of pressing the button has no repeated elements.The minimum possible date is 1970-01-01The maximum possible date is 9999-12-31
# END_DESC

from datetime import datetime
from typing import List, Optional
import itertools as it

def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None) -> int:
    if start_watching is None: 
        start_watching = els[0]
    if end_watching is None: 
        end_watching = els[-1]
    times = [z for z in els if end_watching >= z >= start_watching]
    if len(times) == 0:
        if len(els) % 2 == 0:
            return 0
        else:
            return int((end_watching - start_watching).total_seconds())
    index = els.index(times[0])
    if index % 2 == 1: 
        times = [start_watching] + times
    iters = [iter(times)] * 2
    pairs = list(it.zip_longest(*iters, fillvalue=end_watching))
    return int(sum([(pair[1] - pair[0]).total_seconds() for pair in pairs]))