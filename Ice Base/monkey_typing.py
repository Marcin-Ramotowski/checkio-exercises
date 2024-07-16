#!/usr/bin/env checkio --domain=py run monkey-typing

# p.quote-source {        float: right;        font-size: 10px;    }... If I let my fingers wander idly over the keys of a typewriter it might happen that my screed made an        intelligible sentence. If an army of monkeys were strumming on typewriters they might write all the books in the        British Museum. The chance of their doing so is decidedly more favourable than the chance of the molecules        returning to one half of the vessel.
# 
# A. S. Eddington. The Nature of the Physical World: The Gifford Lectures, 1927.
# 
# 
# 
# "Ford!" he said, "there's an infinite number of monkeys outside who want to talk to us about this script for        Hamlet they've worked out."
# 
# Douglas Adams. The Hitchhikers' Guide to the Galaxy.
# 
# The infinite monkey theoremstates that a monkey hitting keys at random on a typewriter keyboard for an infinite    length of time will almost surely type out a given text, such as the complete works ofJohn Wallis, or more likely,    aDan Brownnovel.
# 
# Let's suppose our monkeys are typing, typing and typing,    and have produced a wide variety of short text segments. Let's try to check them for sensible word inclusions.
# 
# You are given some text potentially including sensible words. You should count how many words are included in the    given text. A word should be whole and may be a part of other word. Text letter case does not matter. Words are    given in lowercase and don't repeat. If a word appears several times in the text, it should be counted only once.
# 
# For example,    text - "Howaresjfhdskfhskdyou?", words - ("how", "are", "you", "hello").    The result will be 3.
# 
# Input:Two arguments.    A text as a string (unicode for py2) and words as a set of strings (unicode for py2).
# 
# Output:The number of words in the text as an integer.
# 
# Precondition:
# 0 < len(text) ≤ 256
# all(3 ≤ len(w) and w.islower() and w.isalpha for w in words)
# 
# 
# END_DESC

def count_words(text: str, words: set) -> int:
    x = 0
    text = text.lower()
    for word in words:
        if text.find(word) != -1: x+= 1
    return x


if __name__ == '__main__':
    print("Example:")
    print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")