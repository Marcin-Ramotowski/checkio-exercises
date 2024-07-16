#!/usr/bin/env checkio --domain=py run solution-for-anything

# We need a solution which can pass any case.    The result of your solution should pass for any comparison with anything.
# 
# You should write the function "checkio" which is called with one argument, the result will be    compared with some other data (==, !=, etc) and the result of that comparison should be True.
# 
# Input:Some data. Maybe that data over there.
# 
# Output:The something as a something-else.
# 
# 
# END_DESC

class AlwaysTrue:
    def __eq__(self, other):  # ==
        return True

    def __ne__(self, other):  # !=
        return True

    def __gt__(self, other):  # >
        return True

    def __lt__(self, other):  # <
        return True

    def __ge__(self, other):  # >=
        return True

    def __le__(self, other):  # <=
        return True

checkio = lambda anything: AlwaysTrue()