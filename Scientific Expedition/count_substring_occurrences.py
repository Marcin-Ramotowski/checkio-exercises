#!/usr/bin/env checkio --domain=py run count-substring-occurrences

# This function should take a main string and a substring as inputs and return the number of occurrences of the substring within the main string. It should not be case-sensitive and may overlap.
# 
# 
# 
# Input:Two strings(str).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert count_occurrences("hello world hello", "hello") == 2
# assert count_occurrences("Hello World hello", "hello") == 2
# assert count_occurrences("hello", "world") == 0
# assert count_occurrences("hello world hello world hello", "world") == 2
# Preconditions:both inputs should be strings: mainStr ∈ string and subStr ∈ string;the main string can have any length, including zero: 0 <= length(mainStr) <= N;the substring should not be an empty string: length(subStr) > 0.
# 
# 
# END_DESC

def count_occurrences(main_str: str, sub_str: str) -> int:
    # your code here
    return 0


print("Example:")
print(count_occurrences("hello world hello", "hello"))

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("appleappleapple", "appleapple") == 2
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")