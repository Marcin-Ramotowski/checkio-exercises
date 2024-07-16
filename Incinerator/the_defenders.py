#!/usr/bin/env checkio --domain=py run the-defenders

# In the previous mission - Army battles, you've learned how to make a battle between 2 armies. But we have only 2 types of units - the Warriors and Knights. Let's add another one - the Defender. It should be the subclass of the Warrior class and have an additionaldefenseparameter, which helps him to survive longer. When another unit hits the defender, he loses a certain amount of his health according to the next formula: enemy attack - self defense (if enemy attack > self defense). Otherwise, the defender doesn't lose his health.
# The basic parameters of the Defender:
# health = 60
# attack = 3
# defense = 2
# 
# 
# Input:The warriors and armies.
# 
# Output:The result of the battle (True or False).
# 
# Precondition:3 types of units
# 
# 
# END_DESC

class Warrior():
    def __init__(self) -> None:
        self.health = 50
        self.attack = 5
        self.defense = 0
    @property
    def is_alive(self):
        return True if self.health > 0 else False

class Knight(Warrior):
    def __init__(self) -> None:
        super().__init__()
        self.attack = 7

class Defender(Warrior):
    def __init__(self) -> None:
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2

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
        power = atacker.attack - defender.defense
        if power > 0:
            defender.health -= power
        m = 0 if m == 1 else 1
        alives = [first.is_alive,second.is_alive]
    return True if first.is_alive else False