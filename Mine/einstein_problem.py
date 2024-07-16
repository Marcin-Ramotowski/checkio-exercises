#!/usr/bin/env checkio --domain=py run einstein-problem

# The Einstein's Puzzleis a well-known logic puzzle.    It is often called Einstein's Puzzle because it is said to have been invented by Albert Einstein as a boy.    However, there is no known evidence for Einstein's or Carroll's authorship.    This puzzle can be modified with various conditions to produce a variety of similar puzzles. For starters, we will    solve a simplified version of the puzzle.
# 
# There are 5 houses on street which are painted 5 different colors:blue,green,red,whiteandyellow.
# In each house lives a person of a different nationality:Brit,Dane,German,NorwegianandSwede.
# These people drink a certain beverage:beer,coffee,milk,teaandwater.
# Smoke a certain brand of cigarettes:Rothmans,Dunhill,PallMall,WinfieldandMarlboro.
# They keep a certain pet:cat,bird,dog,fishandhorse.
# 
# None of the owners have the same pet, smoke the same brand of cigarette, or drink the same beverage.
# 
# You are given a set of "relations". Each relation connects two identifiers in the owner relationships. For example:    "Norwegian-Dunhill" indicates that the Norwegian smokes only Dunhill. "5-dog" indicates that the owner of the 5th    house also owns a dog. Similar to Einstein's version of the problem, we will use only these types of relations.
# 
# The second argument is a question which you need to answer. The question is represented as two words separated by    dash. The first word is a characteristic of the owner while the second is a characteristic (number,    color,nationality, beverage, cigarettes or pet) you need to determine based on the first characteristic. For    example: "horse-cigarettes" asks"What the cigarettes do the owner of the horse smoke?" or "green-number" asks "What    is the street number of the green house?".
# 
# Input:Two arguments. Relations as a tuple of strings and a question as a string.
# 
# Output:The answer as a string.
# 
# How it is used:This mission teaches you something about constraint satisfaction problems within the classic context of an Einstein riddle.
# 
# Precondition:
# All questions have only one possible answer.
# 
# 
# END_DESC

from itertools import chain

COLORS = ['blue', 'green', 'red', 'white', 'yellow']
PETS = ['cat', 'bird', 'dog', 'fish', 'horse']
BEVERAGES = ['beer', 'coffee', 'milk', 'tea', 'water']
CIGARETTES = ['Rothmans', 'Dunhill', 'Pall Mall', 'Winfield', 'Marlboro']
NATIONALITY = ['Brit', 'Dane', 'German', 'Norwegian', 'Swede']
NUMBERS = ['1', '2', '3', '4', '5']
QUESTIONS = ["number", "nationality", "cigarettes", "beverage", "pet", "color"]

CATEGORIES = [NUMBERS,NATIONALITY,CIGARETTES,BEVERAGES,PETS,COLORS]
lexicon = {word:i  for i,category in enumerate(CATEGORIES) for word in category}
ALLELEMENTS = list(chain.from_iterable(CATEGORIES))


def answer(data,quest) -> str:
    # Collecting the link network
    relations = [relation.split('-') for relation in data]
    presentElements = sorted(set(chain.from_iterable(relations)))
    endNumber = len(presentElements)
    networks = []
    checked = 0
    i = 0
    while checked < endNumber:
        toCheck = relations[i]
        visited = [] + toCheck
        network = [] + toCheck
        while len(toCheck) > 0:
            toCheck = sorted(set([rel[0] if rel[0] != word else rel[1] for word in toCheck for rel in relations if word in rel]))
            newComers = [item for item in toCheck if item not in visited]
            visited += newComers
            network += newComers
            toCheck = newComers
        network = sorted(network,key= lambda x:lexicon[x])
        if network not in networks:
            checked += len(network)
            networks.append(network)
        i += 1

    # Connecting matching networks
    puzzles = [net for net in networks if len(net) < 5]
    categories = []
    for puzzle in puzzles:
        category = [lexicon[el] for el in puzzle]
        categories.append(category)
    matched = []
    for i, puzzle1 in enumerate(puzzles):
        l1 = len(puzzle1)
        candidates = sorted([(j,puzzle) for j,puzzle in enumerate(puzzles) if len(puzzle) + l1 <= 6], key = len)
        for candidat in candidates:
            j, puzzle2 = candidat
            if i == j:
                continue
            if [puzzle1, puzzle2] in matched or [puzzle2, puzzle1] in matched:
                continue
            l2 = len(puzzle2)
            test = categories[i] + categories[j]
            if len(set(test)) == l1 + l2:
                networks.remove(puzzle1)
                networks.remove(puzzle2)
                networks.append(sorted(puzzle1 + puzzle2, key= lambda x: lexicon[x]))
                matched.append([puzzle1,puzzle2])
                break

    # Completing the link network with missing words  
    missingWords = [word for word in ALLELEMENTS if word not in presentElements]
    missingWords = {lexicon[word]:word for word in missingWords}
    categories = [] # here will be indexes of categories collected in CATEGORIES
    for net in networks:
        category = [lexicon[el] for el in net]
        categories.append(category)
    for i in range(5):
        net = networks[i]
        if len(net) == 6:
            continue
        numbers = categories[i]
        keys = [key for key in missingWords if key not in numbers]
        values = [missingWords[key] for key in keys]
        net = sorted(net+values, key= lambda x:lexicon[x])
        networks[i] = net

    # Answer
    quest = quest.split('-')
    wanted, searchcategory = quest
    n = QUESTIONS.index(searchcategory)
    found = []
    for net in networks:
        if wanted in net:
            found = net
            break
    for word in CATEGORIES[n]:
        if word in found:
            return word


if __name__ == '__main__':
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'fish-color') == 'green'  # What is the color of the house where the Fish lives?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'tea-number') == '2'  # What is the number of the house where tea is favorite beverage?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'Norwegian-beverage') == 'water'  # What is the favorite beverage of the Norwegian man?