#!/usr/bin/env checkio --domain=py run flatten-a-list-iterator-version

# Nicola likes to categorize all sorts of things.    He categorized a series of numbers and as the result of his efforts,    a simple sequence of numbers became a deeply-nested list.    Sophia and Stephan don't really understand his organization and need to figure out what it all means.    They need your help to understand Nikolas crazy list.
# 
# There is a list iterator which contains integers or    other nested lists iterators which may contain yet more lists iterators and integers which then… you get the idea.    You should put all of the integer values into one flat list.    The order should be as it was in the original list with string representation from left to right.
# After that you have to create an iterator object which is linked to this list.
# 
# We need to hide this program from Nikola by keeping it small.    Because of this,your code should be shorter than 140 characters (with whitespaces).
# 
# Input data:A nested list iterator with integers and other iterators.
# 
# Output data:An iterator object linked to the one-dimensional list with integers.
# 
# Example:
# 
# 
# list(flat_list(iter([1, 2, 3]))) == [1, 2, 3]
# list(flat_list(iter([1, iter([2, 2, 2]), 4]))) == [
#                      1, 2, 2, 2, 4]
# list(flat_list(iter([iter([2]), iter([4, iter([5, 6, iter([6]), 6, 6, 6]), 7])]))) == [
#                      2, 4, 5, 6, 6, 6, 6, 6, 7]
# list(flat_list(iter([-1, iter([1, iter([-2]), 1]), -1]))) == [
#                      -1, 1, -2, 1, -1]
# Precondition:0 ≤ |array| ≤ 100
# ∀ x ∈ array : -232< x < 232or x is a list
# depth < 10
# 
# 
# END_DESC

import re
flat_list =lambda l:iter([int(x.replace('[','').replace(']','')) for x in str(list(l)).split(',') if re.search('\d',x)])

if __name__ == '__main__':
    res = flat_list([1, 2, 3])
    assert hasattr(res, '__iter__'), "your function should return the iterator object"
    assert hasattr(res, '__next__'), "your function should return the iterator object"

    assert list(flat_list(iter([1, 2, 3]))) == [1, 2, 3], "First"
    assert list(flat_list(iter([1, iter([2, 2, 2]), 4]))) == [1, 2, 2, 2, 4], "Second"
    assert list(flat_list(iter([iter([2]), iter([4, iter([5, 6, iter([6]), 6, 6, 6]), 7])]))) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert list(flat_list(iter([-1, iter([1, iter([-2]), 1]), -1]))) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')