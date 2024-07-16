#!/usr/bin/env checkio --domain=py run majority

# We have a List of booleans. Let's check if the majority of elements are true.
# 
# 
# 
# Some cases worth mentioning: 1) an empty list should return false; 2) if trues and falses have an equal amount, function should return false.
# 
# Input:A List of booleans.
# 
# Output:A Boolean.
# 
# 
# END_DESC

is_majority = lambda items: True if items.count(True) > items.count(False) else False