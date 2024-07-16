#!/usr/bin/env checkio --domain=py run fibonacci-spirals-end

# I believe, you have heard aboutFibonacci numbers, which form a respective sequence, where each number is the sum of the two preceding ones. The sequence commonly starts from 0 and 1:
# 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...The sequence may be shown as a tiling with squares whose side lengths are successive Fibonacci numbers. For this mission we use exactly this position of squares:
# 
# If you follow numbers, you see that they form a spiral. Indeed, on the next image the Fibonacci spiral is build: an approximation of the golden spiral, created by drawing circular arcs, connecting the opposite corners of squares in the Fibonacci tiling:
# 
# 
# 
# 
# 
# Now let's put x-axis and y-axis on the image with 0 point in the start of the spiral. Each numbered dot marked is the corner of the square (or the very start of the spiral) of i-th number, where the spiral ends if i-th number is the last one:
# 
# 
# 
# So, for the given sequence number, your function should return the coordinates[x, y]of the end of the spiral (square corner) for the respective Fibonacci number. let's look at the table:
# 
# Sequence number (function input)012345678...Respective Fibonacci number01123581321...Coordinates of the corner (spiral's end)[0, 0][1, -1][2, 0][0, 2][-3, -1][2, -6][10, 2][-3, 15][-24, -6]...
# 
# Input:Integer.
# 
# Output:List of two integers.
# 
# Examples:
# 
# assert fibo_spiral_end(0) == [0, 0]
# assert fibo_spiral_end(1) == [1, -1]
# assert fibo_spiral_end(2) == [2, 0]
# assert fibo_spiral_end(3) == [0, 2]
# 
# 
# 
# END_DESC

def fibo_spiral_end(elem: int) -> list[int]:
    # your code here
    return []


print("Example:")
print(fibo_spiral_end(5))

# These "asserts" are used for self-checking
assert fibo_spiral_end(0) == [0, 0]
assert fibo_spiral_end(1) == [1, -1]
assert fibo_spiral_end(2) == [2, 0]
assert fibo_spiral_end(3) == [0, 2]
assert fibo_spiral_end(4) == [-3, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")