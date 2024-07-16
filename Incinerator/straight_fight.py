#!/usr/bin/env checkio --domain=py run straight-fight

# A new unit type won’t be added in this mission, but instead we’ll add a new tactic -straight_fight(army_1, army_2). It should be the method of the Battle class and it should work as follows:
# at the beginning there will be a few duels between each pair of soldiers from both armies (the first unit against the first, the second against the second and so on). After that all dead soldiers will be removed and the process repeats until all soldiers of one of the armies will be dead. Armies might not have the same number of soldiers. If a warrior doesn’t have an opponent from the enemy army - we’ll automatically assume that he’s won a duel (for example - 9th and 10th units from the first army, if the second has only 8 soldiers).
# 
# Input:The warriors and armies.
# 
# Output:The result of the battle (True or False).
# 
# Precondition:5 types of units, 2 types of battles
# 
# 
# END_DESC

from itertools import zip_longest

class Warrior():
    Health = 50
    def __init__(self) -> None:
        self.maxhealth = 50
        self.attack = 5
    @property
    def health(self):
        return self.Health
    @health.setter
    def health(self,value):
        self.Health = self.maxhealth if value > self.maxhealth else value
    @property
    def is_alive(self):
        return True if self.health > 0 else False

class Knight(Warrior):
    def __init__(self) -> None:
        super().__init__()
        self.attack = 7

class Defender(Warrior):
    Health = 60
    def __init__(self) -> None:
        self.maxhealth = 60
        self.attack = 3
        self.defense = 2

class Vampire(Warrior):
    Health = 40
    def __init__(self) -> None:
        self.maxhealth = 40
        self.attack = 4
        self.vampirism = 50/100

class Lancer(Warrior):
    def __init__(self) -> None:
        super().__init__()
        self.attack = 6

class Healer(Warrior):
    Health = 60
    def __init__(self) -> None:
        super().__init__()
        self.maxhealth = 60
        self.attack = 0
    def heal(self,warrior):
        warrior.health += 2

class Army():
    def __init__(self) -> None:
        self.army = []
    def add_units(self,type,n):
        while n > 0:        
            unit = type()
            self.army.append(unit)
            n -= 1
        return self.army
    def remove_unit(self,x=0):
        self.army.pop(x)
    def remove_fallen(self):
        for soldier in self.army:
            if soldier.health <=0:
                self.army.remove(soldier)


class Battle():
    def fight(self,Army1,Army2):
        while True:
            first, second = Army1.army[0], Army2.army[0]
            neighbor1 = Army1.army[1] if len(Army1.army) > 1 else None
            neighbor2 = Army2.army[1] if len(Army2.army) > 1 else None
            if fight(first,second,(neighbor1,neighbor2)):
                Army2.remove_unit()
                if len(Army2.army) == 0:
                    return True
            else:
                Army1.remove_unit()
                if len(Army1.army) == 0:
                    return False
    def straight_fight(self,Army1,Army2):
        lens = list(map(len,[Army1.army,Army2.army]))
        while 0 not in lens:
            pairs = list(zip_longest(Army1.army,Army2.army))
            for pair in pairs:
                if None not in pair:
                    fight(pair[0],pair[1])
                Army1.remove_fallen()
                Army2.remove_fallen()
                lens = list(map(len,[Army1.army,Army2.army]))
        return True if lens[0] else False


def fight(first,second,neighbors=None):
    fighters = [first,second]
    types = list(map(type,fighters))
    if type(Healer()) in types:
        index = types.index(type(Healer()))
        fighters[index].health = 0
        return True if index==1 else False
    alives = [first.is_alive,second.is_alive]
    m = 0
    while all(alives):
        atacker = fighters[m]
        k = m+1 if m==0 else m-1
        defender = fighters[k]
        power = atacker.attack
        if type(defender) == type(Defender()):
            power -= defender.defense
        if power > 0:
            defender.health -= power
            if type(atacker) == type(Vampire()):
                atacker.health += int(atacker.vampirism * power)

        if neighbors != None:
            neighbor = neighbors[m]
            if type(neighbor) == type(Healer()):
                neighbor.heal(atacker)
            if type(atacker) == type(Lancer()):
                neighbor = neighbors[k]
                if neighbor != None:
                    power = int(power / 2)
                    if type(neighbor) == type(Defender()):
                        power -= neighbor.defense
                    if power > 0:
                        neighbor.health -= power
        m = 0 if m == 1 else 1
        alives = [first.is_alive,second.is_alive]
    return True if first.is_alive else False