#!/usr/bin/env checkio --domain=py run magic-square

# In mathematics amagic squareis an arrangement of numbers    (integers in our case) in a square grid, where the numbers in each row, each column and the numbers in the forward and backward main diagonals, all    sum up to the same number.
# 
# 
# 
# You have been given an incomplete magic square (with a size from 3 to 5). With your coding skills, you must finish the square.    It must be anormalmagic square and contain integers from 1 to n2without repeating.    The square is presented as a list of lists with integers. Zero is used to mark an empty cell.    You should return a completed magic square. The task may have multiple solutions.
# 
# You can read more about the about Magic Squares onWikipedia.
# 
# Input:A partially filled magic square as a list of lists with integers.
# 
# Output:The completed magic square as a list of lists with integers.
# 
# Precondition:3 ≤ |square| ≤ 5
# square_width == square_height
# 
# 
# END_DESC

def checkio(data):
    # replace this for solution
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


if __name__ == "__main__":
    # This part is using only for self-testing.
    def check_solution(func, in_square):
        SIZE_ERROR = "Wrong size of the answer."
        MS_ERROR = "It's not a magic square."
        NORMAL_MS_ERROR = "It's not a normal magic square."
        NOT_BASED_ERROR = "Hm, this square is not based on given template."
        result = func(in_square)
        # check sizes
        N = len(result)
        if len(result) == N:
            for row in result:
                if len(row) != N:
                    print(SIZE_ERROR)
                    return False
        else:
            print(SIZE_ERROR)
            return False
        # check is it a magic square
        # line_sum = (N * (N ** 2 + 1)) / 2
        line_sum = sum(result[0])
        for row in result:
            if sum(row) != line_sum:
                print(MS_ERROR)
                return False
        for col in zip(*result):
            if sum(col) != line_sum:
                print(MS_ERROR)
                return False
        if sum([result[i][i] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False
        if sum([result[i][N - i - 1] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False

        # check is it normal ms
        good_set = set(range(1, N ** 2 + 1))
        user_set = set([result[i][j] for i in range(N) for j in range(N)])
        if good_set != user_set:
            print(NORMAL_MS_ERROR)
            return False
        # check it is the square based on input
        for i in range(N):
            for j in range(N):
                if in_square[i][j] and in_square[i][j] != result[i][j]:
                    print(NOT_BASED_ERROR)
                    return False
        return True

    assert check_solution(checkio, [[2, 7, 6], [9, 5, 1], [4, 3, 0]]), "1st example"

    assert check_solution(checkio, [[0, 0, 0], [0, 5, 0], [0, 0, 0]]), "2nd example"

    assert check_solution(
        checkio, [[1, 15, 14, 4], [12, 0, 0, 9], [8, 0, 0, 5], [13, 3, 2, 16]]
    ), "3rd example"