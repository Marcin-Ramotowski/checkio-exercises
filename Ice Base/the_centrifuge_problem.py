#!/usr/bin/env checkio --domain=py run the-centrifuge-problem

# A centrifuge hasnidentical slots, each big enough to fit one test tube. To prevent this centrifuge from wobbling,kidentical tubes must be placed into these slots so that their mutual center of gravity lies precisely at the center of the centrifuge. This problem was inspired by yet another video “The Centrifuge Problem”, which you may watch below. Alternatively, whose eyes read faster than their ears listen can check out Matt Baker’s post“The Balanced Centrifuge Problem”.
# 
# 
# 
# So, balancingktest tubes intonslots turns out to be possible if and only if bothk, n-kcan be expressed as sums of prime factors ofn, repetition of factors allowed. For example, whennequals 6 whose prime factors are 2 and 3, the centrifuge can hold 0, 2, 3, 4 (= 2 + 2) or 6 (= 3 + 3) test tubes.     However, there is no possible way to balance 1 or 5 test tubes in six slots. Even though 5 = 2 + 3 satisfies the first part of the rule, there is no way to counterbalance the remaining empty slot, which is required despite the counterintuitive fact that empty slots weigh nothing!
# 
# 
# 
# This function does not actually need to construct the balanced configuration ofktest tubes, but merely determine whether at least one balanced configuration exists for the givenn, k.
# 
# Input:Two integers(int)
# 
# Output:Logic value(bool).
# 
# Examples:
# 
# assert balanced_centrifuge(6, 3) == True
# assert balanced_centrifuge(7, 0) == True
# assert balanced_centrifuge(15, 8) == False
# The mission was taken from Python CCPS 109. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def balanced_centrifuge(n: int, k: int) -> bool:
    # your code here
    return False


print("Example:")
print(balanced_centrifuge(6, 3))

# These "asserts" are used for self-checking
assert balanced_centrifuge(6, 3) == True
assert balanced_centrifuge(7, 0) == True
assert balanced_centrifuge(15, 8) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")