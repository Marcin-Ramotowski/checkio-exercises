#!/usr/bin/env checkio --domain=py run box-probability

# To start the game they put several black and white pearls in one of the boxes.    Each robot hasNmoves, after which the initial set is being restored for the next game.    Each turn, the robot takes a pearl out of the box and puts one of the opposite color back.    The winner is the one who takes the white pearl on theNthmove.
# 
# Our robots don't like uncertainty, that's why they want to know the probability of drawing a white pearl on the Nth move.    The probability is a value between 0 (0% chance or will not happen) and 1 (100% chance or will happen).    The result is a float from 0 to 1 with two decimal digits of precision (±0.01).
# 
# You are given a start set of pearls as a string that contains "b" (black) and "w" (white) and the number of the move    (N).    The order of the pearls does not matter.
# 
# 
# 
# Input:The start sequence of the pearls as a string and the move number as an integer.
# 
# Output:The probability for a white pearl as a float.
# 
# Precondition:0 < N ≤ 20
# 0 < |pearls| ≤ 20
# 
# 
# 
# END_DESC

from fractions import Fraction


def checkio(marbles: str, step: int) -> float:
    n = len(marbles)
    if step == 1:
        return marbles.count('w') / n
    probs = [(Fraction(marbles.count('b'), n), marbles.replace('b', 'w', 1)),
             (Fraction(marbles.count('w'), n), marbles.replace('w', 'b', 1))]
    for i in range(1, step-1):
        iter_probs = iter(probs)
        probs = []
        for prob, balls in iter_probs:
            score1 = prob * Fraction(balls.count('b'), n), balls.replace('b', 'w', 1)
            score2 = prob * Fraction(balls.count('w'), n), balls.replace('w', 'b', 1)
            probs.append(score1)
            probs.append(score2)
    score = sum([prob * Fraction(balls.count('w'), n) for prob, balls in probs])
    return round(float(score),2)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio('bbw', 3))

    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    print("Coding complete? Click 'Check' to earn cool rewards!")