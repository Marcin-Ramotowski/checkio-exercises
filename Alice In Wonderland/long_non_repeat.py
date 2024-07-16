#!/usr/bin/env checkio --domain=py run long-non-repeat

# There are four substring missionsthat were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# A very similar to the first is the second mission of the series with only one distinction is that you should look in a completely different way. You need to find the first longest substring with all unique letters. For example, in substring "abca" we have two substrings with unique letters "abc" and "bca", but we should take the first one, so the answer is "abc".
# 
# Input:String.Output:String.
# 
# 
# 
# 
# 
# 
# END_DESC

def non_repeat(text):
    """
        the longest substring without repeating chars
    """
    if len(text) < 2:
        return text
    if len(set(text)) == 1:
        return text[0]
    text += '*'
    subs, sub = [], ''
    for char in text:
        if char not in sub and char != '*':
            sub += char
        else:
            subs.append(sub)
            if char != '*':
                sub = sub[1:] + char
                if sub.count(char) > 1:
                    i = sub.index(char)
                    sub = sub[0:i] + sub[i+1:]
    return max(subs, key=len)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')