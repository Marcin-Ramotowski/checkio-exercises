#!/usr/bin/env checkio --domain=py run all-permutations

# Given a string, return all possiblepermutationsof its characters, sorted alphabetically.
# 
# 
# 
# Input:String(str).
# 
# Output:Iterableof strings(str).
# 
# Examples:
# 
# assert list(string_permutations("ab")) == ["ab", "ba"]
# assert list(string_permutations("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]
# assert list(string_permutations("a")) == ["a"]
# assert list(string_permutations("abcd")) == [
#     "abcd",
#     "abdc",
#     "acbd",
#     "acdb",
#     "adbc",
#     "adcb",
#     "bacd",
#     "badc",
#     "bcad",
#     "bcda",
#     "bdac",
#     "bdca",
#     "cabd",
#     "cadb",
#     "cbad",
#     "cbda",
#     "cdab",
#     "cdba",
#     "dabc",
#     "dacb",
#     "dbac",
#     "dbca",
#     "dcab",
#     "dcba",
# ]
# 
# END_DESC

from collections.abc import Iterable


def string_permutations(s: str) -> Iterable[str]:
    # your code here
    return []


print("Example:")
print(list(string_permutations("ab")))

# These "asserts" are used for self-checking
assert list(string_permutations("ab")) == ["ab", "ba"]
assert list(string_permutations("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]
assert list(string_permutations("a")) == ["a"]
assert list(string_permutations("abcd")) == [
    "abcd",
    "abdc",
    "acbd",
    "acdb",
    "adbc",
    "adcb",
    "bacd",
    "badc",
    "bcad",
    "bcda",
    "bdac",
    "bdca",
    "cabd",
    "cadb",
    "cbad",
    "cbda",
    "cdab",
    "cdba",
    "dabc",
    "dacb",
    "dbac",
    "dbca",
    "dcab",
    "dcba",
]

print("The mission is done! Click 'Check Solution' to earn rewards!")