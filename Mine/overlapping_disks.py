#!/usr/bin/env checkio --domain=py run overlapping-disks

# Given a list ofdiskson the two-dimensional plane represented as tuples(x, y, r)so thatx, yis thecenter pointandris theradiusof that disk, count how many pairs of disksintersect.
# 
# Two disks(x1, y1, r1)and(x2, y2, r2)intersect if and only if they satisfy thePythagoreaninequality(x2-x1)**2+(y2-y1)**2<=(r1+r2)**2.
# 
# Note how this precise formula runs on pure integer arithmetic whenever its arguments are integers, so no square roots or any other irrational numbers gum up the works with all that decimal noise. (This formula also uses the operator<=to count twokissingdisks as an intersecting pair).
# 
# For this problem, crudely looping through all possible pairs of disks would work, but also become horrendously inefficient for large lists. However, asweep line algorithmcan solve this problem not justeffectively, but alsoefficiently(a crucial but often overlooked “eff-ing” distinction) by looking at a far fewer pairs of disks.
# 
# Here is a scheme for[(0, 0, 3), (6, 0, 3), (6, 6, 3), (0, 6, 3)]:
# 
# 
# 
# Input:Listof tuples(tuple)of integers(int).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert overlapping_disks([(0, 0, 3), (6, 0, 3), (6, 6, 3), (0, 6, 3)]) == 4
# assert overlapping_disks([(4, -1, 3), (-3, 3, 2), (-3, 4, 2), (3, 1, 4)]) == 2
# assert (
#     overlapping_disks([(-10, 6, 2), (6, -4, 5), (6, 3, 5), (-9, -8, 1), (1, -5, 3)])
#     == 2
# )
# assert (
#     overlapping_disks(
#         [
#             (2, 2, 1),
#             (3, 3, 1),
#             (4, 4, 2),
#             (5, 5, 2),
#             (6, 6, 3),
#             (7, 7, 3),
#             (8, 8, 4),
#             (9, 9, 4),
#             (10, 10, 5),
#             (11, 11, 5),
#             (12, 12, 6),
#             (13, 13, 6),
#             (14, 14, 7),
#             (15, 15, 7),
#             (16, 16, 8),
#             (17, 17, 8),
#             (18, 18, 9),
#             (19, 19, 9),
#             (20, 20, 10),
#             (21, 21, 10),
#             (22, 22, 11),
#             (23, 23, 11),
#             (24, 24, 12),
#             (25, 25, 12),
#             (26, 26, 13),
#             (27, 27, 13),
#             (28, 28, 14),
#             (29, 29, 14),
#             (30, 30, 15),
#             (31, 31, 15),
#             (32, 32, 16),
#             (33, 33, 16),
#             (34, 34, 17),
#             (35, 35, 17),
#             (36, 36, 18),
#             (37, 37, 18),
#             (38, 38, 19),
#             (39, 39, 19),
#             (40, 40, 20),
#             (41, 41, 20),
#             (42, 42, 21),
#             (43, 43, 21),
#             (44, 44, 22),
#             (45, 45, 22),
#             (46, 46, 23),
#             (47, 47, 23),
#             (48, 48, 24),
#             (49, 49, 24),
#             (50, 50, 25),
#             (51, 51, 25),
#             (52, 52, 26),
#             (53, 53, 26),
#             (54, 54, 27),
#             (55, 55, 27),
#             (56, 56, 28),
#             (57, 57, 28),
#             (58, 58, 29),
#             (59, 59, 29),
#             (60, 60, 30),
#             (61, 61, 30),
#             (62, 62, 31),
#             (63, 63, 31),
#             (64, 64, 32),
#             (65, 65, 32),
#             (66, 66, 33),
#             (67, 67, 33),
#             (68, 68, 34),
#             (69, 69, 34),
#             (70, 70, 35),
#             (71, 71, 35),
#             (72, 72, 36),
#             (73, 73, 36),
#             (74, 74, 37),
#             (75, 75, 37),
#             (76, 76, 38),
#             (77, 77, 38),
#             (78, 78, 39),
#             (79, 79, 39),
#             (80, 80, 40),
#             (81, 81, 40),
#             (82, 82, 41),
#             (83, 83, 41),
#             (84, 84, 42),
#             (85, 85, 42),
#             (86, 86, 43),
#             (87, 87, 43),
#             (88, 88, 44),
#             (89, 89, 44),
#             (90, 90, 45),
#             (91, 91, 45),
#             (92, 92, 46),
#             (93, 93, 46),
#             (94, 94, 47),
#             (95, 95, 47),
#             (96, 96, 48),
#             (97, 97, 48),
#             (98, 98, 49),
#             (99, 99, 49),
#             (100, 100, 50),
#         ]
#     )
#     == 2563
# )
# If you feel yourself in need of a hint, click this line.Sweep through the space from left to right for all relevant x-coordinate values and maintain theset of active disksat the moment. Each individual disk(x, y, r)enters the active set when the vertical sweep line reaches the x-coordinatex-r, and leaves the active set when the sweep line reachesx+r. At the time when a disk enters the active set, you need to look for its intersections only in this active set.
# 
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def overlapping_disks(disks: list[tuple[int, int, int]]) -> int:
    # your code here
    return 0


print("Example:")
print(overlapping_disks([(0, 0, 3), (6, 0, 3), (6, 6, 3), (0, 6, 3)]))

# These "asserts" are used for self-checking
assert overlapping_disks([(0, 0, 3), (6, 0, 3), (6, 6, 3), (0, 6, 3)]) == 4
assert overlapping_disks([(4, -1, 3), (-3, 3, 2), (-3, 4, 2), (3, 1, 4)]) == 2
assert (
    overlapping_disks([(-10, 6, 2), (6, -4, 5), (6, 3, 5), (-9, -8, 1), (1, -5, 3)])
    == 2
)
assert (
    overlapping_disks(
        [
            (2, 2, 1),
            (3, 3, 1),
            (4, 4, 2),
            (5, 5, 2),
            (6, 6, 3),
            (7, 7, 3),
            (8, 8, 4),
            (9, 9, 4),
            (10, 10, 5),
            (11, 11, 5),
            (12, 12, 6),
            (13, 13, 6),
            (14, 14, 7),
            (15, 15, 7),
            (16, 16, 8),
            (17, 17, 8),
            (18, 18, 9),
            (19, 19, 9),
            (20, 20, 10),
            (21, 21, 10),
            (22, 22, 11),
            (23, 23, 11),
            (24, 24, 12),
            (25, 25, 12),
            (26, 26, 13),
            (27, 27, 13),
            (28, 28, 14),
            (29, 29, 14),
            (30, 30, 15),
            (31, 31, 15),
            (32, 32, 16),
            (33, 33, 16),
            (34, 34, 17),
            (35, 35, 17),
            (36, 36, 18),
            (37, 37, 18),
            (38, 38, 19),
            (39, 39, 19),
            (40, 40, 20),
            (41, 41, 20),
            (42, 42, 21),
            (43, 43, 21),
            (44, 44, 22),
            (45, 45, 22),
            (46, 46, 23),
            (47, 47, 23),
            (48, 48, 24),
            (49, 49, 24),
            (50, 50, 25),
            (51, 51, 25),
            (52, 52, 26),
            (53, 53, 26),
            (54, 54, 27),
            (55, 55, 27),
            (56, 56, 28),
            (57, 57, 28),
            (58, 58, 29),
            (59, 59, 29),
            (60, 60, 30),
            (61, 61, 30),
            (62, 62, 31),
            (63, 63, 31),
            (64, 64, 32),
            (65, 65, 32),
            (66, 66, 33),
            (67, 67, 33),
            (68, 68, 34),
            (69, 69, 34),
            (70, 70, 35),
            (71, 71, 35),
            (72, 72, 36),
            (73, 73, 36),
            (74, 74, 37),
            (75, 75, 37),
            (76, 76, 38),
            (77, 77, 38),
            (78, 78, 39),
            (79, 79, 39),
            (80, 80, 40),
            (81, 81, 40),
            (82, 82, 41),
            (83, 83, 41),
            (84, 84, 42),
            (85, 85, 42),
            (86, 86, 43),
            (87, 87, 43),
            (88, 88, 44),
            (89, 89, 44),
            (90, 90, 45),
            (91, 91, 45),
            (92, 92, 46),
            (93, 93, 46),
            (94, 94, 47),
            (95, 95, 47),
            (96, 96, 48),
            (97, 97, 48),
            (98, 98, 49),
            (99, 99, 49),
            (100, 100, 50),
        ]
    )
    == 2563
)

print("The mission is done! Click 'Check Solution' to earn rewards!")