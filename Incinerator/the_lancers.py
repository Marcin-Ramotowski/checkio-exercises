#!/usr/bin/env checkio --domain=py run the-lancers

# It seems that the Warrior, Knight, Defender and Vampire are not enough to win the battle. Let's add one more powerful unit type - the Lancer.
# Lancer should be the subclass of the Warrior class and should attack in a specific way - when he hits the other unit, he also deals a 50% of the deal damage to the enemy unit, standing behind the firstly assaulted one (enemy defense makes the deal damage value lower - consider this).
# The basic parameters of the Lancer:
# health = 50
# attack = 6
# 
# 
# Input:The warriors and armies.
# 
# Output:The result of the battle (True or False).
# 
# Precondition:5 types of units
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

class Defender(Warrior):
    def __init__(self) -> None:
        self.health = 60
        self.attack = 3
        self.defense = 2

class Vampire(Warrior):
    def __init__(self) -> None:
        self.health = 40
        self.attack = 4
        self.vampirism = 50/100

class Lancer(Warrior):
    def __init__(self) -> None:
        super().__init__()
        self.attack = 6

class Army():
    def __init__(self) -> None:
        self.army = []
        self.isLancer = False
    def add_units(self,type,n):
        while n > 0:
            if type == Lancer and not(self.isLancer):
                self.isLancer = True
            unit = type()
            self.army.append(unit)
            n -= 1
        return self.army
    def remove_unit(self):
        self.army.pop(0) #remove defeated unit


class Battle():
    def fight(self,Army1,Army2):
        gamemode = 1 if Army1.isLancer or Army2.isLancer else 0
        while True:
            first, second = Army1.army[0], Army2.army[0]
            if gamemode:
                neighbor1 = Army1.army[1] if len(Army1.army) > 1 else None
                neighbor2 = Army2.army[1] if len(Army2.army) > 1 else None
                score = fight(first,second,(neighbor1,neighbor2))
            else:
                score = fight(first,second)
            if score:
                Army2.remove_unit()
                if len(Army2.army) == 0:
                    return True
            else:
                Army1.remove_unit()
                if len(Army1.army) == 0:
                    return False
    
def fight(first,second,neighbors=None):
    fighters = [first,second]
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