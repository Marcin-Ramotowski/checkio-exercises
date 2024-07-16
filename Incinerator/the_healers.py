#!/usr/bin/env checkio --domain=py run the-healers

# The battle continues and each army is losing good warriors. Let's try to fix that and add a new unit type - the Healer.
# Healer won't be fighting (his attack = 0, so he can't deal the damage). But his role is also very important - every time the allied soldier hits the enemy, the Healer will heal the allie, standing right in front of him by +2 health points with theheal()method. Note that the health after healing can't be greater than the maximum health of the unit.For example, if the Healer heals the Warrior with 49 health points, the Warrior will have 50 hp, because this is the maximum for him.
# The basic parameters of the Healer:
# health = 60
# attack = 0
# 
# 
# Input:The warriors and armies.
# 
# Output:The result of the battle (True or False).
# 
# Precondition:6 types of units
# 
# 
# END_DESC

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
        self.army.pop(x) #remove defeated unit


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

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    assert freelancer.health == 14    
    priest.heal(freelancer)
    assert freelancer.health == 16

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")