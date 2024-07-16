#!/usr/bin/env checkio --domain=py run identify-block

# This mission uses a 4x4 grid. Each square is numbered from 1 to 16 in row-major order.
# You are given 4 numbers(a set of integers).These numbers represent the positions of each square on the grid and a whole block if all the squares are adjacent.
# 
# You have to identify the kind of block. (Refer to the following image or comment of initial code for the kind of block).
# The answer is an upper-case alphabet letter ('I', 'J', 'L', 'O', 'S', 'T' or 'Z'). If it’s not a block, then return None.
# 
# The block is placed anywhere on the grid and can be rotated (0, 90, 180 or 270 degrees).
# 
# 
# 
# Input:4 numbers (a set of integers)
# 
# Output:the kind of block (an alphabet letter or         None)
# 
# 
# END_DESC

def identify_block(numbers):
    rows = (
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    )
    columns = []
    numbers = list(numbers)
    numbers.sort()
    for i in range(0,4):
        column = [row[i] for row in rows]
        columns.append(column)

    rowsNumbers = []
    columnsNumbers = []
    for number in numbers:
        for row in rows:
            if number in row:
                x = rows.index(row)
                rowsNumbers.append(x)
                break
        for column in columns:
            if number in column:
                y = columns.index(column)
                columnsNumbers.append(y)

    checkRows = set(rowsNumbers)
    checkColumns = set(columnsNumbers)
    l1 = len(checkRows)
    l2 = len(checkColumns)

    if l1 == 1 or l2 == 1:
        return 'I'

    if l1 == 2 and l2 == 2:
        checkrows = list(checkRows)
        checkcolumns = list(checkColumns)
        diffRow = abs(checkrows[1] - checkrows[0])
        diffCol = abs(checkcolumns[1] - checkcolumns[0])
        if diffRow == 1 and diffCol == 1:
            return 'O'

    if (l1 == 2  and l2 == 3) or (l1 == 3 and l2 == 2):
        amountsRows = [rowsNumbers.count(value) for value in checkRows ]
        if 3 in amountsRows:
            checker1 = numbers[1] - numbers[0]
            checker2 = numbers[-1] - numbers[-2]
            if checker1 == 4 or checker2 == 4:
                return 'J'
            if checker1 == 2 or  checker2 == 2:
                return 'L'
            if checker1 == 3 or checker2 == 3:
                return 'T'
        if amountsRows == [1, 2, 1] or [2, 2]:
            i = 0
            diffs = []
            while i < 3:
                z = numbers[i+1] - numbers[i]
                diffs.append(z)
                i += 1
            if amountsRows == [2, 2]:
                if diffs == [1, 2, 1]:
                    return "S"
                if diffs == [1, 4, 1]:
                    return "Z"
            if amountsRows == [1, 2, 1]:
                if diffs == [4, 1, 4]:
                    return "S"
                if diffs == [3, 1, 3]:
                    return "Z"

        for value in checkColumns:
            y = columnsNumbers.count(value)
            if y == 3:
                checkColumns2 = list(checkColumns.copy())
                checkColumns2.remove(value)
                checker1 = numbers[1] - numbers[0]
                checker2 = numbers[-1] - numbers[-2]
                checker3 = numbers[2] - numbers[1]
                if checker1 == 1:
                    value2 = checkColumns2[0]
                    if value > value2:
                        return 'L'
                    else:
                        return 'J'
                if checker2 == 1:
                    value2 = checkColumns2[0]
                    if value < value2:
                        return 'L'
                    else:
                        return 'J'
                if checker3 == 1:
                    return 'T'
    return None

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert identify_block({10, 13, 14, 15}) == 'T', 'T'
    assert identify_block({1, 5, 9, 6}) == 'T', 'T'
    assert identify_block({2, 3, 7, 11}) == 'L', 'L'
    assert identify_block({4, 8, 12, 16}) == 'I', 'I'
    assert identify_block({3, 1, 5, 8}) == None, 'None'
    print('"Run" is good. How is "Check"?')