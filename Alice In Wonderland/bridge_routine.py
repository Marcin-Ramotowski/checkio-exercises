#!/usr/bin/env checkio --domain=py run bridge-routine

# The trick taking power of a bridge hand is estimated withMilton Work point count, of which we shall implement a version that is simple enough for beginners of eitherPythonor the game ofbridge!
# 
# Looking at a bridge hand that consists of thirteen cards as tuples(rank, suit):
# 
# give it 4 points for eachace, 3 points for eachking, 2 points for eachqueen, and 1 point for eachjack. Thisraw point countis then adjusted with the following rules.if the hand contains one 4-cards suit and three 3-cards suits, subtract one point for beingflat. (Flat hands rarely play as well as non-flat hands of equal point count.)add 1 point for every suit that has 5 cards, 2 points for every suit that has 6 cards, and 3 points for every suit with 7 cards or longer. (Shape is power for the declarer.)if thetrumpis anything other than"notrump", add 5 points for everyvoid(that is, suit without any cards in it) and 3 points for everysingleton(that is, a suit with exactly one card), both of these for any other suit than thetrumpsuit. (Voids and singletons are great when you are playing a suit contract, but very bad in a notrump contract. Being void or a singleton in the trump suit is, of course, extremely bad!)Hands are often given in abbreviated form that makes their relevant aspects easier to visualize at a glance. In this abbreviated shorthand form, suits are always listed in the exact order ofspades, hearts, diamonds, clubs, so no special symbols are needed to show which suit is which. The ranks in each suit are listed as letters  from"AKQJ"foraces, facesand allspotcards lower thanjackare written out as the same letter"x"to indicate that its exact spot value is irrelevant for the play mechanics of that hand. These letters must be listed in descending order of ranks AKQJx. If some suit isvoid, that is, the hand contains no cards of that suit, that suit is abbreviated with a minus sign character "-". The shorthand forms for the individual suits are separated using single spaces, with no trailing whitespace.
# 
# Your function must return a number of points and a shorthand form of a given hand.
# 
# Input:Two arguments.Listof tuples of two strings(str). String(str).
# 
# Output:Tuple or list of integer(int)and string(str).
# 
# Examples:
# 
# assert list(
#     bridge_routine(
#         [
#             ("four", "spades"),
#             ("five", "spades"),
#             ("ten", "hearts"),
#             ("six", "hearts"),
#             ("queen", "hearts"),
#             ("jack", "hearts"),
#             ("four", "hearts"),
#             ("two", "hearts"),
#             ("three", "diamonds"),
#             ("seven", "diamonds"),
#             ("four", "diamonds"),
#             ("two", "diamonds"),
#             ("four", "clubs"),
#         ],
#         "diamonds",
#     )
# ) == [8, "xx QJxxxx xxxx x"]
# assert list(
#     bridge_routine(
#         [
#             ("three", "spades"),
#             ("queen", "hearts"),
#             ("jack", "hearts"),
#             ("eight", "hearts"),
#             ("six", "diamonds"),
#             ("nine", "diamonds"),
#             ("jack", "diamonds"),
#             ("ace", "diamonds"),
#             ("nine", "clubs"),
#             ("king", "clubs"),
#             ("jack", "clubs"),
#             ("five", "clubs"),
#             ("ace", "clubs"),
#         ],
#         "clubs",
#     )
# ) == [20, "x QJx AJxx AKJxx"]
# assert list(
#     bridge_routine(
#         [
#             ("three", "spades"),
#             ("queen", "hearts"),
#             ("jack", "hearts"),
#             ("eight", "hearts"),
#             ("six", "diamonds"),
#             ("nine", "diamonds"),
#             ("jack", "diamonds"),
#             ("ace", "diamonds"),
#             ("nine", "clubs"),
#             ("king", "clubs"),
#             ("jack", "clubs"),
#             ("five", "clubs"),
#             ("ace", "clubs"),
#         ],
#         "spades",
#     )
# ) == [17, "x QJx AJxx AKJxx"]
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def bridge_routine(
    hand: list[tuple[str, str]], trump="notrump"
) -> tuple[int, str] | list[int, str]:
    # your code here
    return []


print("Example:")
print(
    list(
        bridge_routine(
            [
                ("four", "spades"),
                ("five", "spades"),
                ("ten", "hearts"),
                ("six", "hearts"),
                ("queen", "hearts"),
                ("jack", "hearts"),
                ("four", "hearts"),
                ("two", "hearts"),
                ("three", "diamonds"),
                ("seven", "diamonds"),
                ("four", "diamonds"),
                ("two", "diamonds"),
                ("four", "clubs"),
            ],
            "diamonds",
        )
    )
)

# These "asserts" are used for self-checking
assert list(
    bridge_routine(
        [
            ("four", "spades"),
            ("five", "spades"),
            ("ten", "hearts"),
            ("six", "hearts"),
            ("queen", "hearts"),
            ("jack", "hearts"),
            ("four", "hearts"),
            ("two", "hearts"),
            ("three", "diamonds"),
            ("seven", "diamonds"),
            ("four", "diamonds"),
            ("two", "diamonds"),
            ("four", "clubs"),
        ],
        "diamonds",
    )
) == [8, "xx QJxxxx xxxx x"]
assert list(
    bridge_routine(
        [
            ("three", "spades"),
            ("queen", "hearts"),
            ("jack", "hearts"),
            ("eight", "hearts"),
            ("six", "diamonds"),
            ("nine", "diamonds"),
            ("jack", "diamonds"),
            ("ace", "diamonds"),
            ("nine", "clubs"),
            ("king", "clubs"),
            ("jack", "clubs"),
            ("five", "clubs"),
            ("ace", "clubs"),
        ],
        "clubs",
    )
) == [20, "x QJx AJxx AKJxx"]
assert list(
    bridge_routine(
        [
            ("three", "spades"),
            ("queen", "hearts"),
            ("jack", "hearts"),
            ("eight", "hearts"),
            ("six", "diamonds"),
            ("nine", "diamonds"),
            ("jack", "diamonds"),
            ("ace", "diamonds"),
            ("nine", "clubs"),
            ("king", "clubs"),
            ("jack", "clubs"),
            ("five", "clubs"),
            ("ace", "clubs"),
        ],
        "spades",
    )
) == [17, "x QJx AJxx AKJxx"]

print("The mission is done! Click 'Check Solution' to earn rewards!")