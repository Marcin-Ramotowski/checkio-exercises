#!/usr/bin/env checkio --domain=py run count-inversions

# In computer science and discrete mathematics,    aninversionis a pair of places in a sequence where the elements in these places are out of their natural order. So, if we use    ascending order for a group of numbers, then an inversion is when larger numbers appear before lower number in a    sequence.
# 
# Check out this example sequence: (1, 2, 5, 3, 4, 7, 6) and we can see here three inversions
# - 5 and 3;
# - 5 and 4;
# - 7 and 6.
# 
# 
# You are given a sequence of unique numbers and you should count the number of inversions in this sequence.
# 
# Input:A sequence as a tuple of integers.
# 
# Output:The inversion number as an integer.
# 
# Precondition:2 < len(sequence) < 200
# len(sequence) == len(set(sequence))
# all(-100 < x < 100 for x in sequence)
# 
# 
# END_DESC

def count_inversion(seq):
    inversions = 0
    for i,item in enumerate(seq):
        for number in seq[i+1:]:
            if number < item:
                inversions += 1
    return inversions


if __name__ == '__main__':
    print("Example:");
    print(count_inversion([1, 2, 5, 3, 4, 7, 6]));

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")