#!/usr/bin/env checkio --domain=py run digits-doublets

# .story .shadow {        float: left;        /*padding: 10px;*/        margin: 10px;        border: black;        /*box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/        /*-moz-box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/        /*-webkit-box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/    }    .story .left {        float: left;    }    .story .right {        float: right;    }    .story .title {        font-weight: bold;        margin: 20px 0 20px 0;    }Doublets, sometimes known as Word ladder, is a word game invented by Charles Dodgson (aka Lewis Carroll).    A doublets puzzle begins with two words.    To solve the puzzle one must find a chain of different words to link the two together such that the two adjacent words    differ by one letter.
# 
# For Example:FLOUR⇒ FLOOR ⇒ FLOOD ⇒ BLOOD ⇒    BROOD ⇒ BROAD ⇒BREAD
# 
# The Robots like using digits more than letters, so we’ve changed the rules a little.    You are given the list of numbers with exactly the same length and you must find the shortest chain of numbers    to link the first number to the last like you would with the words.
# 
# For Example. There is a list [123, 991, 323, 321, 329, 121, 921, 125, 999].    The shortest way from the first to the last is:123⇒ 121 ⇒ 921 ⇒ 991 ⇒999
# 
# You should write a function that receives a list of numbers (positive integers) and    returns the shortest route as a list of numbers.
# 
# Input:Numbers as a list of integers.
# 
# Output:The shortest chain from the first to the last number as a list of integers.
# 
# Precondition:Numbers have the same length
# ∀ x ∈ numbers : 100 ≤ x < 1000
# 
# 
# 
# END_DESC

def checkio(numbers):
    work = list(map(str, numbers))
    last = work[-1]
    l = len(last)

    def checker(previous, actual):
        x = 0
        for pair in zip(previous, actual):
            if pair[0] == pair[1]:
                x += 1
        return x == 2

    def corrector(score):
        i = 1
        js = []
        while i < len(score):
            a = score[i]
            b = score[i - 1]
            j = 0
            for x, y in zip(b, a):
                if x != y:
                    js.append(j)
                    if len(js) > 1:
                        if js[-1] == js[-2]:
                            score.remove(b)
                    break
                j += 1
            i += 1
        return score

    queue = [(work[0], work[0])]
    visited = set()
    while queue:
        temp, path = queue.pop()
        if temp in visited:
            continue
        if temp == last:
            score = [path[i:i + l] for i in range(0, len(path), l)]
            score = corrector(score)
            score = list(map(int,score))
            return score
        similar = [number for number in work if checker(temp, number)]
        for n in similar:
            if n not in visited:
                queue.append((n, path + n))
        visited.add(temp)
    return []

print(checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]))
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 656, 654], "Third, [456, 454, 654] is correct too"