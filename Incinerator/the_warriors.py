#!/usr/bin/env checkio --domain=py run the-warriors

# I'm sure that many of you have some experience with computer games. But have you ever wanted to change the game so that the characters or a game world would be more consistent with your idea of the perfect game? Probably, yes.
# In this mission (and in several subsequent ones, related to it) you’ll have a chance "to sit in the developer's chair" and create the logic of a simple game about battles.
# Let's start with the simple task - one-on-one duel. You need to create the classWarrior, the instances of which will have 2 parameters - health (equal to 50 points) and attack (equal to 5 points), and 1 property - is_alive, which can be True (if warrior's health is > 0) or False (in the other case). In addition you have to create the second unit type - Knight, which should be the subclass of the Warrior but have the increased attack - 7. Also you have to create a functionfight(), which will initiate the duel between 2 warriors and define the strongest of them. The duel occurs according to the following principle:
# Every turn, the first warrior will hit the second and this second will lose his health in the same value as the attack of the first warrior. After that, if he is still alive, the second warrior will do the same to the first one.
# The fight ends with the death of one of them. If the first warrior is still alive (and thus the other one is not anymore), the function should returnTrue,Falseotherwise.
# 
# Input:The warriors.
# 
# Output:The result of the duel (True or False).
# 
# Precondition:2 types of unitsAll given fights have an end (for all missions).
# 
# 
# END_DESC

class Warrior():
    def __init__(self) -> None:
        self.health = 50
        self.attack = 5
    @property
    def is_alive(self):
        return True if self.health > 0 else False

class Knight(Warrior):
    def __init__(self) -> None:
        super().__init__()
        self.attack = 7

def fight(first,second):
    fighters = [first,second]
    alives = [first.is_alive,second.is_alive]
    whose_move = 0
    while all(alives):
        fighters[whose_move+1 if whose_move==0 else whose_move-1].health -= fighters[whose_move].attack
        whose_move = 0 if whose_move == 1 else 1
        alives = [first.is_alive,second.is_alive]
    return True if first.is_alive else False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")