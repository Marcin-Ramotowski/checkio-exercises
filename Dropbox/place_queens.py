#!/usr/bin/env checkio --domain=py run place-queens

# Almost everyone in the world knows about the ancient gameChessand has at least a basic understanding of its rules.    Ancient humans loved this game of skill and strategy and    our Robots are attempting to examine all tricks to becoming Chess Grandmasters.    Today they are trying to solve the 8-Queen problem as written in an old chess-manuscript.
# 
# Chess is a two-player strategy game played on a checkered game board laid out in eight rows    (called ranks and denoted with numbers 1 to 8) and    eight columns (called files and denoted with letters a to h) of squares.    Each square of the chessboard is identified by a unique coordinate pair    — a letter and a number (ex, "a1", "h8", "d6").    For this mission we only need to concern ourselves with Queens.    The Queen can move any number of squares along the rank, file, or diagonal axis.
# 
# You should place eight chess Queens on an 8×8 chessboard so that no two Queens threaten each other.    For this challenge, we have already placed one or more Queens on the board,    so you will need to finish the placement.    In addition, each Queen may be considered as part of it’s army,    meaning every Queen could possible be a threat to every other Queen on the board.
# 
# You are given a set of square coordinates where we have placed Queens already.    You should finish this set and return the full set of the coordinates for all eight Queens.    If it's not possible -- return an empty set.
# Be careful - an initial position could possibly threaten another Queen right off the bat.
# 
# 
# 
# Input:Placed Queens coordinates as a set of strings.
# 
# Output:Eight Queens coordinates as a set of strings or an empty set.
# 
# Precondition:
# 0 < placed < 8
# 
# 
# 
# END_DESC

import numpy as np


def place_queens(placed: set) -> set:
    board = np.zeros((8, 8))
    for letter, number in placed:
        point = (8 - int(number), ord(letter)-97)
        if not is_safe(board, point):
            return set()
        board[point] = 1
    new_queens = []
    n = 8 - len(placed)
    indexes = [i for i, row in enumerate(board) if 1 not in row]
    nrRow = startRow = indexes[0]
    nrCol = 0
    x = 1

    while len(new_queens) < n:
        position = (nrRow, nrCol)
        safe = is_safe(board, position)
        while not safe and nrCol < 8:
            nrCol += 1
            safe = is_safe(board, (nrRow, nrCol))
        if nrCol > 7:
            if nrRow == startRow:
                return set()
            nrRow, nrCol = new_queens.pop()
            board[nrRow, nrCol] = 0
            nrCol += 1
            x -= 1
            continue
        else:
            new_queens.append((nrRow, nrCol))
            board[nrRow, nrCol] = 1
            if x == len(indexes):
                break
            nrRow = indexes[x]
            nrCol = 0
            x += 1
    for a, b in new_queens:
        x = chr(b + 97)
        y = str(8 - a)
        placed.add(''.join(x+y))
    return placed


def is_safe(board, pos):
    maxRow, maxCol = board.shape
    row, col = pos
    if col == maxCol:
        return False
    else:
        column = board[:, col]
        Row = board[row]
    if any(column) or any(Row):
        return False

    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i, j]:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < maxCol:
        if board[i, j]:
            return False
        i -= 1
        j += 1

    i, j = row + 1, col + 1
    while i < maxRow and j < maxCol:
        if board[i, j]:
            return False
        i += 1
        j += 1

    i, j = row + 1, col - 1
    while i < maxRow and j >= 0:
        if board[i, j]:
            return False
        i += 1
        j -= 1

    return True


if __name__ == '__main__':
    print(place_queens({"b2", "c4", "d6", "e8"}))
    print(place_queens({"a1", "h8"}))