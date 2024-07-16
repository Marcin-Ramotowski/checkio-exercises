#!/usr/bin/env checkio --domain=py run halloween-monsters

# You have to call the monsters from another world in preparation for Halloween.
# 
# You are given a string as an input value.    You have to use it to make monster names and return themaximumnumber.    You can call only9kinds of monsters:
# 
# frankensteinghostjackmummyskeletonvampirewerewolfwitchzombieNOTE:You can make multiple monster names of the same kind.You don't need to use all the characters.If you can't make a monster name, return 0.Input:The spell (a string).
# 
# Output:A number of monsters (an integer).
# 
# Precondition:
# 
# all(re.fullmatch('[a-z]', i) for i in input)len(input) ≤ 100How it is used:To calculate materials and products.
# 
# 
# END_DESC

MONSTERS = ['jack', 'ghost', 'mummy', 'witch', 'zombie', 'vampire', 'skeleton', 'werewolf', 'frankenstein']
repeats = ['mummy', 'skeleton', 'werewolf', 'frankenstein'] # monster names with repeated letters


def halloween_monsters(spell: str):
    x = 0
    monsters = []
    isAll = False
    while not(isAll):
        isAll = True
        i = 0
        while i < len(MONSTERS):
            monster = MONSTERS[i]
            isMatched = True
            if monster not in repeats:
                for letter in monster:
                    if letter not in spell:
                        isMatched = False
                        break
            else:
                for letter in set(monster):
                    if spell.count(letter) < monster.count(letter):
                        isMatched = False
                        break
            if isMatched:
                x += 1
                i = 0
                monsters.append(monster)
                isAll = False
                for letter in monster:
                    spell = spell.replace(letter, '', 1)
            i += 1
        return monsters


print(MONSTERS)
print(halloween_monsters('leumooeeyzwwmmirbmf'))


if __name__ == '__main__':
    assert halloween_monsters('casjokthg') == 2, 'jack ghost'
    assert halloween_monsters('leumooeeyzwwmmirbmf') == 3, 'mummy zombie werewolf'
    assert halloween_monsters('nafrweiicttwneshhtikcn') == 3, 'witch witch frankenstein'
    assert halloween_monsters('kenoistcepajmlvre') == 2, 'skeleton vampire (not jack)'
    assert halloween_monsters('miaimavrurymepepv') == 2, 'vampire vampire (not mummy)'
    print("Your spell seem to be okay. It's time to check.")