#!/usr/bin/env checkio --domain=py run broken-window

# You have to restore the broken window glass.
# 
# You are given a list of lists as input values.Each list of integers represents a missing piece.It always has a horizontal base, which forms the upper or lower side of the window.Each integer represents the height from the base and is a value measured at equal intervals from the left edge. Therefore, the length of the list represents the width.
# 
# The answer should be returned in the two lists (the upper list and lower list in that order).
# 
# In the output each piece is represented in the order given as input (starting with 0).The bases of the pieces in the same list must always be adjacent to each other.(In other words, one piece doesn't form both the upper and lower side of the window.)It is not necessary to consider turning over piece.Input:The pieces of the broken window (list of lists of integers).
# 
# Output:The list of top pieces and list of bottom pieces (both are lists of integers).
# 
# Precondition:
# 2 ≤ len(input)2 ≤ len(piece)1 ≤ width of window ≤ 201 ≤ height of window ≤ 18
# 
# 
# END_DESC

from typing import List, Tuple


def broken_window(pieces: List[List[int]]) -> Tuple[List[int], List[int]]:
    return []


if __name__ == '__main__':

    def checker(func, pieces):
        answer = func(pieces)

        if not (isinstance(answer, (tuple, list))
                and len(answer) == 2
                and isinstance(answer[0], list) and isinstance(answer[1], list)):
            print('wrong type:', answer)
            return False

        if set(answer[0]+answer[1]) != set(range(len(pieces))):
            print('wrong value:', answer)
            return False

        tops = [list(reversed(pieces[t])) for t in answer[0]]
        bottoms = [pieces[b] for b in answer[1]]
        height = set()

        top = tops.pop(0)
        bottom = bottoms.pop(0)
        while True:
            height |= set(map(sum, zip(top, bottom)))
            if len(top) < len(bottom) and tops:
                bottom = bottom[len(top)-1:]
                top = tops.pop(0)
            elif len(top) > len(bottom) and bottoms:
                top = top[len(bottom)-1:]
                bottom = bottoms.pop(0)
            elif len(top) == len(bottom):
                if tops and bottoms:
                    top = tops.pop(0)
                    bottom = bottoms.pop(0)
                elif not tops and not bottoms:
                    break
                else:
                    return False
            else:
                return False

        return len(height) == 1

    print("Example:")
    print(broken_window([[0, 1], [0, 1]]))

    assert checker(broken_window, [[0, 3, 4, 1], [4, 0], [3, 0], [0, 1, 4, 0]])
    assert checker(broken_window, [[0, 1], [0, 1]])
    print("Coding complete? Click 'Check' to earn cool rewards!")