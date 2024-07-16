#!/usr/bin/env checkio --domain=py run magic-with-5-cards

# code { background: transparent; white-space: nowrap; }    code.r { color: red; }    code.b { color: #163e69; }    table { border-collapse: collapse; }    th, td { border: 1px solid #163e69; padding: 5px; }    th, td:first-child { text-align: center; font-weight: bold; }    th:first-child { border: 0px; }    p, li { text-align: justify; }Well, it's an automatic magic trick, that I will explain in a moment.You will have to create two functions. A function namedbotwhich will take five cards,an integer and return four of them ; and a function namedmagicianwhich will take four cards,the same integer and return the fifth one.
# 
# The trick use thestandard 52-card deck.Cards will be represented like'A ♥','3 ♦','K ♠','Q ♣','J ♦'(♣for clubs,♦for diamonds,♥for hearts,♠for spades,A for Ace, J for Jack, Q for Queen and K for King).
# We will soon need to compare cards. The deck order isA ♣<A ♦<A ♥<A ♠<2 ♣<....To compare two cards, look ranksA < 2 < ... < 10 < J < Q < K,then suits♣<♦<♥<♠(same order than with letters:club < diamond < heart < spade).
# 
# The card the bot choose to hide and the order of the four cards the bot says is crucial for the magicianso he can guess the fifth one. There are five cards, but only four suits so there are at least two cardsfrom the same suit, we name themcard Aandcard B. The bot will hide one and say the other,but which one? Imagine the thirteen cards in a circle,clockwise.If going fromcard Atocard Bon this circle is quicker than going fromcard Btocard A,then we will hidecard B, saycard A, and the distance fromcard Atocard Bis noted as delta (it's necessarily a number between one and six). We still have three cards to say,and since there are six ways to tell three cards, we can transmit "delta information".Thecard Awill be the starting point, then by "adding" delta tocard A,the magician can "guess" the fifth card.
# Sort the three remaining cards, according to the above order, and note themC1,C2andC3.If delta is 5 or 6, putC1first, if delta is 3 or 4, putC2first, andC3otherwise.You still have two cards to say, tell them in order if delta is odd (1, 3, 5), and in reverse order otherwise (2, 4, 6).
# At this point, the bot have two things to say: thecard A, and a list of three cards.If we repeat this magic trick multiple times and if we always say thecard Afirst,John might notice it since the fifth card andcard Ahave the same suit.So we are not going to always tellcard Afirst. The first time, we will say it first,the second time, say it second, ..., the fifth time, say it first again...
# 
# botmagicianInputFive strings and an integerFour strings and an integerOutputA list/tuple of four stringsA string
# 
# END_DESC

RANKS = tuple('A 2 3 4 5 6 7 8 9 10 J Q K'.split())
SUITS = tuple('♣♦♥♠')


def bot(*cards, n=1):
    """Determine four cards the bot has to say to the magician."""
    # Obviously not always just the first four, put your code here instead.
    return cards[:4]


def magician(*cards, n=1):
    """Determine the fifth card with only four cards."""
    # Obviously not a random card, put your code here instead.
    from random import choice
    deck = [f'{r} {s}' for r in RANKS for s in SUITS]
    for card in cards:
        deck.remove(card)
    return choice(deck)


if __name__ == '__main__':
    assert list(bot('A ♥', '3 ♦', 'K ♠', 'Q ♣', 'J ♦')) == ['J ♦', 'A ♥', 'Q ♣', 'K ♠']
    assert magician('J ♦', 'A ♥', 'Q ♣', 'K ♠') == '3 ♦'

    assert list(bot('10 ♦', 'J ♣', 'Q ♠', 'K ♥', '7 ♦', n=2)) == ['Q ♠', '7 ♦', 'J ♣', 'K ♥']
    assert magician('Q ♠', '7 ♦', 'J ♣', 'K ♥', n=2) == '10 ♦'