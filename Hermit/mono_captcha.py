#!/usr/bin/env checkio --domain=py run mono-captcha

# Let's teach Stephan to recognize simple numbers. The Robots use monospaced fonts with low resolution.    You can see the font on the picture below. This font has noise immunity to one-pixel error.
# 
# 
# 
# Your program should read the number shown in an image encoded as a binary matrix.    Each digit can contain a wrong pixel, but no more than one for each digit.    The space between digits is equal to one pixel (just think about "1" which is narrower than other letters, but has a width of 3 pixels).
# 
# 
# 
# Input:An image as a list of lists with 1 or 0.
# 
# Output:The number as an integer.
# 
# Precondition:matrix_rows == 5
# 5 ≤ matrix_columns < 30
# ∀ x ∈ matrix : x == 0 or x == 1
# digit_width == 3
# Each digit contains no more than one wrong pixel.
# digits_space == 1
# 
# 
# END_DESC

from typing import List
import numpy as np


def checkio(image: List[List[int]]) -> int:
    PATTERNS = {
        '1': np.array([[0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]),
        '2': np.array([[1, 1, 1], [0, 0, 1], [0, 1, 1], [1, 0, 0], [1, 1, 1]]),
        '3': np.array([[1, 1, 1], [0, 0, 1], [0, 1, 0], [0, 0, 1], [1, 1, 1]]),
        '4': np.array([[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]]),
        '5': np.array([[1, 1, 1], [1, 0, 0], [1, 1, 0], [0, 0, 1], [1, 1, 0]]),
        '6': np.array([[0, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [0, 1, 1]]),
        '7': np.array([[1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 0, 0]]),
        '8': np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]]),
        '9': np.array([[0, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 0]]),
        '0': np.array([[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 1]])
    }
    image = np.array(image, int)
    end = image.shape[1] - 1
    score = ''
    digits = [image[:, i + 1:i + 4] for i in range(0, end, 4)]

    for digit in digits:
        for key, pattern in PATTERNS.items():
            comparison = digit != pattern
            differences = comparison.sum()
            if differences < 2:
                score += key
                break
    return int(score)