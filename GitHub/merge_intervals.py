#!/usr/bin/env checkio --domain=py run merge-intervals

# You are given a sequence of intervals, as tuples of ints where the tuples are sorted by  their first element in ascending order.
# It is your task to minimize the number of intervals by merging those that intersect or  by removing intervals fitting into another one.
# 
# Since the range of values for the intervals is restricted to integers, you must also  merge those intervals between which no value can be found.
# 
# An example:
# Let's say you've got these 5 intervals:1..6, 3..5, 7..10, 9..12 and 14..16.1..6 and 3..5
# 3..5fits into1..6, so3..5must disappear.1..6 and 7..10
# Even though the intervals do not intersect, there can not be a value of type int      between them, so they have to be merged to the new interval1..10.1..10 and 9..12
# These intervals do intersect, because9 < 10,      so they have to be merged to the new interval1..12.1..12 and 14..16
# These two intervals do not intersect, so they must not be merged.So the intervals to be returned are:
# 1..12 and 14..16
# 
# Input:A sequence of intervals as a  list of tuples of 2 ints, sorted by their first element.
# 
# Output:The merged intervals as a list of tuples of 2 ints, sorted by their first element.
# 
# Precondition:
# intervals == sorted(intervals, key=lambda x: x[0])  # sorted by 1st element of      the tuplesinterval[0] <= interval[1]
# 
# 
# END_DESC

# Stensen's solution
def merge_intervals(intervals):
    if not intervals: return []
    intervals = sorted(intervals)
    L, H = intervals[0]
    for l, h in intervals[1:]:
        if l - H == 1: H = h
        elif l <= H: H = max(H, h)
        else: yield L, H; L, H = l, h
    yield L, H