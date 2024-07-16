#!/usr/bin/env checkio --domain=py run broken-clock

# We have a broken clock. We know how quickly it runs or lags over a specific period of time.    At first, the clock is set to the correct time, but after a while it begins    to display an incorrect time... But instead of correcting the clock each time,     we will use an algorithm to calculate the correct time by accounting for     the difference compared to the actual current time. Of course we will have access to     the correct time for each day. In addition, you can be certain that     the correct starting time and current actual time fall on the same day.     For this mission, time is measured in a 24 hour format.
# 
# You are given three values.    The first is the correct starting time.     The second is the current time displayed on the broken clock (which is incorrect).     Time is given as strings in the format "hh:mm:ss" (Examples: "01:16:59" and "23:00:13").    The third value is a description of the clock error in the format"+(-)N [second, minute, hour](s) at M [second, minute, hour](s)".     For Example "+1 second at 10 seconds" --     the clock is 1 second fast for every 10 seconds of actual time and     "-5 minutes at 5 hours" -- the clock lags 5 minutes for every 5 hours of actual time.
# 
# You should calculate the real time with the given values.    The result should be rounded down to the nearest second (use floor or int).
# 
# Let's examine one example -- '00:00:00', '00:00:30', '+2 seconds at 6 seconds'.
# 0th step: The real and fake time is "00:00:00".
# When the real time is "00:00:06", the fake time is "00:00:08".
# At real "00:00:18", fake is "00:00:24".
# At real "00:00:21", fake is "00:00:28".
# At real "00:00:22", fake is "00:00:29.333...".
# At real "00:00:22.5", fake is "00:00:30".
# So answer is "00:00:22.5" after rounding down "00:00:22"
# 
# Input:Three arguments.    Correct starting time, current wrong time and broken clock descriptions as strings.
# 
# Output:The real time as a string.
# 
# Precondition:
# "wrong_time" is later than "starting_time".
# 
# 
# END_DESC

from datetime import datetime, timedelta

def broken_clock(time1,time2,desc):
    isRushing = True if desc[0] == "+" else False
    descs = desc.split(" at ")
    desc1, desc2 = descs
    h, m, s = map(int, time1.split(":"))
    h2, m2, s2 = map(int, time2.split(":"))
    time1 = datetime(1970, 1, 1, h, m, s)
    time2 = datetime(1970, 1, 1, h2, m2, s2)
    delta = time2 - time1
    indexes = [0,0]
    for i, desc in enumerate(descs):
        for j, char in enumerate(desc):
            if char.isspace():
                indexes[i] = j
                break
    i1, i2 = indexes
    tu1 = 'second' if 'second' in desc1 else 'minute' if 'minute' in desc1 else 'hour'
    tu2 = 'second' if 'second' in desc2 else 'minute' if 'minute' in desc2 else 'hour'
    n1 = abs(int(desc1[0:i1]))
    n2 = int(desc2[0:i2])
    if tu1 != 'second':
        temp = timedelta(minutes=n1) if tu1 == 'minute' else timedelta(hours=n1)
        n1 = temp.total_seconds()
    if tu2 != 'second':
        temp = timedelta(minutes=n2) if tu2 == 'minute' else timedelta(hours=n2)
        n2 = temp.total_seconds()
    diff = n1 / n2 + 1 if isRushing else 1 - n1/n2
    flow = int(round(delta.total_seconds() / diff,2))
    score = time1 + timedelta(seconds=flow)
    return str(score).split()[1]