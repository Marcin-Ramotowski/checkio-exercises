#!/usr/bin/env checkio --domain=py run r-mahjong-i-break-hand-into-sets

# This mission is the beginning of a series of missions dedicated to Japanese game "riichi mahjong". In each subsequent mission, your task will become more difficult.
# 
# The meaning of riichi mahjong is to collect a certain combination of cards by discarding and taking cards. In this it resembles poker, only there are much more cards in it, and the rounds are longer. The cards in this game are called tiles, and each player has 14 of them.
# 
# In riichi, tiles come in five suits. Three of them are digital: man, pin and so; each of the digital suits contains tiles from 1 to 9. The fourth suit is dragons; it includes three types of tiles — a white dragon, a red dragon and a green dragon. The fifth is the wind. As it is easy to guess, it contains four winds according to the names of the cardinal directions. Each tile comes in four copies.
# 
# Now let's agree on the tile designations. The suits of man, pin and so will be abbreviated as "m", "p" and "s", and dragons and winds as "d", "w". Red, white and green dragons will be denoted by "r", "w" and "g". The "north", "south", etc. winds are encrypted in the same way as the cardinal directions. Thus, for example, "6 man" is written as "m6", and "green dragon" is written as "dg".
# 
# The finished hand should, as already mentioned, contain a certain combination of tiles. More precisely, it should contain four sets and a pair. There are two types of sets — chi and pona. Chi is a sequence of three tiles of the same suit in a row, for example: "m123" or "p567". In this case, combinations of the type "m912" are not allowed. Pons are three identical tiles of the same suit, that is, "s999" or "p444". A pair is two identical tiles.
# 
# Example of a hand: 234678 man, 234 pin, 888 so, two south winds. This hand contains four sets (234 pin, 234 man, 678 man chi; 888 so— pont) and a pair (two south winds). This will be encoded as "m2", "m3", "m4", "m6", "m7", "m8", "p2", "p3", "p4", "s8", "s8", "s8", "ws", "ws".
# 
# The goal of the mission is to split this set of tiles ("hand") into sets.
# 
# Input data:One argument (list type) is strings encoding tiles, in any order.
# 
# Output data:List of strings-sets (sorted).
# 
# Example:
# 
# 
# riichi_mahjong_sets(['m2', 's9', 'p9', 'dg', 's3', 's2', 'm1', 's8', 'dg', 'p9', 'dg', 's7', 's1', 'm3']) == ['dggg', 'm123', 'p99', 's123', 's789']
# 
# END_DESC

def riichi_mahjong_sets(hand: list) -> list:
    # your code here
    return sorted([])  # you must sort resulting list before returning


print("Example:")
print(
    riichi_mahjong_sets(
        [
            "m2",
            "s9",
            "p9",
            "dg",
            "s3",
            "s2",
            "m1",
            "s8",
            "dg",
            "p9",
            "dg",
            "s7",
            "s1",
            "m3",
        ]
    )
)

# These "asserts" are used for self-checking
assert riichi_mahjong_sets(
    ["m7", "s6", "p2", "m9", "s5", "wn", "s3", "p4", "s4", "p3", "s5", "m8", "s7", "wn"]
) == ["m789", "p234", "s345", "s567", "wnn"]
assert riichi_mahjong_sets(
    ["s7", "p4", "s6", "m8", "m4", "m3", "m8", "m8", "m2", "p6", "m4", "s5", "p5", "m4"]
) == ["m234", "m44", "m888", "p456", "s567"]
assert riichi_mahjong_sets(
    ["s8", "s7", "p2", "s4", "s9", "s3", "s5", "s1", "s6", "m5", "s2", "p2", "m3", "m4"]
) == ["m345", "p22", "s123", "s456", "s789"]
assert riichi_mahjong_sets(
    ["s8", "s9", "m1", "ws", "dr", "s7", "dr", "m9", "ws", "m9", "m2", "dr", "m3", "ws"]
) == ["drrr", "m123", "m99", "s789", "wsss"]

print("Now, what about 'Check solution'?")