#!/usr/bin/env checkio --domain=py run the-vampires

# So we have 3 types of units: the Warrior, Knight and Defender. Let's make the battles even more epic and add another type - the Vampire!
# Vampire should be the subclass of the Warrior class and have the additionalvampirismparameter, which helps him to heal himself. When the Vampire hits the other unit, he restores his health by +50% of the dealt damage (enemy defense makes the dealt damage value lower).
# The basic parameters of the Vampire:
# health = 40
# attack = 4
# vampirism = 50%
# 
# 
# You should store vampirism attribute as an integer (50 for 50%). It will be needed to make this solution evolutes to fit one of the next challenges of this saga.
# 
# Input:The warriors and armies.
# 
# Output:The result of the battle (True or False).
# 
# Precondition:4 types of units
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

class Army():
    def __init__(self) -> None:
        self.army = []
    def add_units(self,type,n):
        while n > 0:
            unit = type()
            self.army.append(unit)
            n -= 1
        return self.army
    def remove_unit(self):
        self.army.pop(0) #remove defeated unit

class Battle():
    def fight(self,Army1,Army2):
        while True:
            first, second = Army1.army[0], Army2.army[0]
            if fight(first,second):
                Army2.remove_unit()
                if len(Army2.army) == 0:
                    return True
            else:
                Army1.remove_unit()
                if len(Army1.army) == 0:
                    return False
    

def fight(first,second):
    fighters = [first,second]
    alives = [first.is_alive,second.is_alive]
    m = 0
    while all(alives):
        atacker = fighters[m]
        defender = fighters[m+1 if m==0 else m-1]
        power = atacker.attack
        if type(defender) == type(Defender()):
            power -= defender.defense
        if power > 0:
            defender.health -= power
            if type(atacker) == type(Vampire()):
                atacker.health += int(atacker.vampirism * power)
        m = 0 if m == 1 else 1
        alives = [first.is_alive,second.is_alive]
    return True if first.is_alive else False