#!/usr/bin/env checkio --domain=py run flatten-list

# Nicola likes to categorize all sorts of things.    He categorized a series of numbers and as the result of his efforts,    a simple sequence of numbers became a deeply-nested list.    Sophia and Stephan don't really understand his organization and need to figure out what it all means.    They need your help to understand Nikolas crazy list.
# 
# There is a list which contains integers or    other nested lists which may contain yet more lists and integers which then… you get the idea.    You should put all of the integer values into one flat list.    The order should be as it was in the original list with string representation from left to right.
# 
# We need to hide this program from Nikola by keeping it small and easy to hide.    Because of this,your code should be shorter than 140 characters (with whitespaces).
# 
# Input data:A nested list with integers.
# 
# Output data:The one-dimensional list with integers.
# 
# Example:
# 
# 
# flat_list([1, 2, 3]) == [1, 2, 3]
# flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
# flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
# flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]
# Precondition:0 ≤ |array| ≤ 100
# ∀ x ∈ array : -232< x < 232or x is a list
# depth < 10
# 
# 
# END_DESC

import re
flat_list =lambda l:[int(x.replace('[','').replace(']','')) for x in str(l).split(',') if re.search('\d',x)]