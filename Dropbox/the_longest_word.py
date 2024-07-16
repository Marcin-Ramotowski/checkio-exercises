#!/usr/bin/env checkio --domain=py run the-longest-word

# This function should take a string without punctuation marks as an input and return the longest word in the string. If there are multiple words of the same length, return the first one that appears.
# 
# 
# 
# Input:String(str).
# 
# Output:String(str).
# 
# Examples:
# 
# assert longest_word("hello world") == "hello"
# assert longest_word("openai gpt-4") == "openai"
# assert longest_word("this is a sentence") == "sentence"
# assert longest_word("the quick brown fox") == "quick"
# Preconditions:sentence ∈ string;length(sentence) >= 0.
# 
# 
# END_DESC

def longest_word(sentence: str) -> str:
    # your code here
    return ""


print("Example:")
print(longest_word("hello world"))

# These "asserts" are used for self-checking
assert longest_word("hello world") == "hello"
assert longest_word("openai gpt-4") == "openai"
assert longest_word("this is a sentence") == "sentence"
assert longest_word("the quick brown fox") == "quick"
assert longest_word("jumped over the lazy dog") == "jumped"
assert longest_word("typescript is great") == "typescript"
assert longest_word("the answer is 42") == "answer"
assert longest_word("to be or not to be") == "not"
assert longest_word("that is the question") == "question"
assert longest_word("") == ""
assert longest_word(" ") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")