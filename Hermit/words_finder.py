#!/usr/bin/env checkio --domain=py run words-finder

# Sophie has found a stash books and she wants to find information about the ancients who lived on the islands.    Unfortunately, she does not have a text search module and needs some help.    Let's write a program to help her search for keywords on the pages of a book.
# 
# You are given some plain text (without tags) and a string with keywords (or parts of words, or letters) separated by spaces.    You will need to find all the keywords and put these words into "<span></span>" wrappers to highlight them for Sophie.    You can ignore upper or lower cases for the key words, but the original letter cases in the text should remain.
# 
# For the cases when keywords contain or intersect each other you should highlight the larger word without nested span tags.    Let's look it with example.
# The text"Hello World! Or LOL"and keywords"hell world or lo".
# The word"World"contains two keywords thus we tag only larger part"<span>World</span>".
# "Hello"contains two intersected words"hell"and"lo"and we tag the larger part again"<span>Hello</span>".
# Be careful, a result like"<span>Hel<span>lo</span></span>"is considered wrong because it contains nested tags.
# 
# Input:Two arguments. A text and key words as strings.
# 
# Output:The text with wrapped key words.
# 
# 
# END_DESC

import re
from itertools import chain


def merge_intervals(intervals):
    intervals = sorted(intervals)
    if not intervals: return []
    L, H = intervals[0]
    for l, h in intervals[1:]:
        if l < H: H = max(H, h)
        else: yield L, H; L, H = l, h
    yield L, H


def checkio(text: str, words: str):
    if not text:
        return ''
    elif not words:
        return text

    words = re.split(' +', words)
    matches = (re.finditer(word, text, re.IGNORECASE) for word in words)
    matches = chain.from_iterable(matches)
    intervals = merge_intervals(map(lambda x: x.span(), matches))

    # pattern = words if ' ' not in words else '(' + re.sub(' +', ')|(', words) + ')'
    # matches = re.finditer(pattern, text, re.IGNORECASE)
    c = 0
    for x, y in intervals:
        new = '<span>' + text[x+c:y+c] + '</span>'
        text = text[:x + c] + new + text[y + c:]
        c += 13
    return text


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio("This is only a text example for task example.", "example") ==
            "This is only a text <span>example</span> for task <span>example</span>."), "Simple test"

    assert (checkio("Python is a widely used high-level programming language.", "pyThoN") ==
            "<span>Python</span> is a widely used high-level programming language."), "Ignore letters cases, but keep original"

    assert (checkio("It is experiment for control groups with similar distributions.", "is im") ==
            "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions."), "Several subwords"

    assert (checkio("The National Aeronautics and Space Administration (NASA).", "nasa  THE") ==
            "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>)."), "two spaces"

    assert (checkio("Did you find anything?", "word space tree") ==
            "Did you find anything?"), "No comments"

    assert (checkio("Hello World! Or LOL", "hell world or lo") ==
            "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"), "Contain or intersect"