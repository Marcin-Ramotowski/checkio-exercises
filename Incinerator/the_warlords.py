#!/usr/bin/env checkio --domain=py run the-warlords

# 
# END_DESC

from itertools import zip_longest, dropwhile

class Warrior():
    def __init__(self) -> None:
        self.maxhealth = 50
        self.health = 50
        self.attack = 5
    @property
    def is_alive(self):
        return True if self.health > 0 else False
    def equip_weapon(self,weapon):
        self.maxhealth += weapon.health if self.maxhealth + weapon.health >= 0 else -self.maxhealth
        self.health += weapon.health if self.health + weapon.health >= 0 else -self.health
        self.attack += weapon.attack if self.attack + weapon.attack > 0 else -self.attack
        if self.__class__ == Defender().__class__ or self.__class__ == Warlord().__class__:
            self.defense += weapon.defense if self.defense + weapon.defense > 0 else -self.defense
        if self.__class__ == Vampire().__class__:
            self.vampirism += weapon.vampirism if self.vampirism + weapon.vampirism > 0 else -self.vampirism
        if self.__class__ == Healer().__class__:
            self.heal_power += weapon.heal_power if self.heal_power + weapon.heal_power > 0 else - self.heal_power

class Knight(Warrior):
    def __init__(self) -> None:
        super().__init__()
        self.attack = 7

class Defender(Warrior):
    def __init__(self) -> None:
        self.maxhealth = 60
        self.health = 60
        self.attack = 3
        self.defense = 2

class Vampire(Warrior):
    def __init__(self) -> None:
        self.maxhealth = 40
        self.health = 40
        self.attack = 4
        self.vampirism = 50
    def heal(self,power):
        energy = self.health + int(self.vampirism/100 * power)
        self.health = energy if energy < self.maxhealth else self.maxhealth

class Lancer(Warrior):
    def __init__(self) -> None:
        super().__init__()
        self.attack = 6

class Healer(Warrior):
    def __init__(self) -> None:
        self.maxhealth = 60
        self.health = 60
        self.attack = 0
        self.heal_power = 2
    def heal(self,warrior):
        energy = warrior.health + self.heal_power
        warrior.health = energy if energy < warrior.maxhealth else warrior.maxhealth

class Warlord(Warrior):
    def __init__(self) -> None:
        self.maxhealth = 100
        self.health = 100
        self.attack = 4
        self.defense = 2

PRIORITY = {Healer().__class__:0, Lancer().__class__:1,  Warlord().__class__:3}


class Weapon():
    def __init__(self,health=0,attack=0,defense=0,vampirism=0,heal_power=0) -> None:
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power

class Sword(Weapon):
    def __init__(self) -> None:
        self.health = 5
        self.attack = 2
        self.defense,self.vampirism,self.heal_power = 0,0,0

class Shield(Weapon):
    def __init__(self) -> None:
        self.health = 20
        self.attack = -1
        self.defense = 2
        self.vampirism, self.heal_power = 0,0

class GreatAxe(Weapon):
    def __init__(self) -> None:
        self.health = -15
        self.attack = 5
        self.defense = -2
        self.vampirism = 10
        self.heal_power = 0

class Katana(Weapon):
    def __init__(self) -> None:
        self.health = -20
        self.attack = 6
        self.defense = -5
        self.vampirism = 50
        self.heal_power = 0

class MagicWand(Weapon):
    def __init__(self) -> None:
        self.health = 30
        self.attack = 3
        self.defense, self.vampirism = 0,0
        self.heal_power = 3

class Army():
    def __init__(self) -> None:
        self.units = []
        self.isWarlord = False
    def add_units(self,type,n):
        while n > 0:
            if type == Warlord:
                if not(self.isWarlord):
                    self.isWarlord = True
                else:
                    n -= 1
                    continue
            unit = type()
            self.units.append(unit)
            n -= 1
        return self.units
    def remove_unit(self,x=0):
        self.units.pop(x) #remove defeated unit
    def remove_fallen(self):
        for soldier in self.units:
            if soldier.health <=0:
                self.units.remove(soldier)
    def move_units(self):
        if self.isWarlord:
            self.units = sorted(self.units, key=lambda x: PRIORITY[x.__class__] if x.__class__ in PRIORITY else 2)
            first = self.units[0]
            if first.__class__ == Healer().__class__:
                i, zmiennik = list(dropwhile(lambda x: x[1].__class__ == Healer().__class__, enumerate(self.units)))[0]
                if zmiennik != None:
                    self.units.pop(i)
                    self.units.insert(0, zmiennik)


class Battle():
    def fight(self,Army1,Army2):
        Army1.move_units()
        Army2.move_units()
        while True:
            first, second = Army1.units[0], Army2.units[0]
            neighbor1 = Army1.units[1] if len(Army1.units) > 1 else None
            neighbor2 = Army2.units[1] if len(Army2.units) > 1 else None
            if fight(first,second,(neighbor1,neighbor2)):
                Army2.remove_unit()
                Army2.move_units()
                if len(Army2.units) == 0:
                    return True
            else:
                Army1.remove_unit()
                Army1.move_units()
                if len(Army1.units) == 0:
                    return False
    def straight_fight(self,Army1,Army2):
        Army1.move_units()
        Army2.move_units()
        lens = list(map(len,[Army1.units,Army2.units]))
        while 0 not in lens:
            pairs = list(zip_longest(Army1.units,Army2.units))
            for pair in pairs:
                if None not in pair:
                    fight(pair[0],pair[1])
                Army1.remove_fallen()
                Army1.move_units()
                Army2.remove_fallen()
                Army2.move_units()
                lens = list(map(len,[Army1.units,Army2.units]))
        return True if lens[0] else False


def fight(first, second, neighbors=None):
    fighters = [first, second]
    attacks = [fighter.attack for fighter in fighters]
    if 0 in attacks:
        index = attacks.index(0)
        fighters[index].health = 0
        return True if index==1 else False
    alives = [first.is_alive,second.is_alive]
    m = 0
    while all(alives):
        atacker = fighters[m]
        k = m+1 if m == 0 else m-1
        defender = fighters[k]
        power = atacker.attack
        if defender.__class__ == Defender().__class__ or defender.__class__ == Warlord().__class__:
            power -= defender.defense
        if power > 0:
            defender.health -= power
            if atacker.__class__ == Vampire().__class__:
                atacker.heal(power)

        if neighbors != None:
            neighbor = neighbors[m]
            if neighbor.__class__ == Healer().__class__:
                neighbor.heal(atacker)
            if atacker.__class__ == Lancer().__class__:
                neighbor = neighbors[k]
                if neighbor != None:
                    power = int(power / 2)
                    if neighbor.__class__ == Defender().__class__ or neighbor.__class__ == Warlord().__class__:
                        power -= neighbor.defense
                    if power > 0:
                        neighbor.health -= power
        m = 0 if m == 1 else 1
        alives = [first.is_alive,second.is_alive]
    return True if first.is_alive else False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
	ronald = Warlord()
	heimdall = Knight()

	assert fight(heimdall, ronald) == False

	my_army = Army()
	my_army.add_units(Warlord, 1)
	my_army.add_units(Warrior, 2)
	my_army.add_units(Lancer, 2)
	my_army.add_units(Healer, 2)

	enemy_army = Army()
	enemy_army.add_units(Warlord, 3)
	enemy_army.add_units(Vampire, 1)
	enemy_army.add_units(Healer, 2)
	enemy_army.add_units(Knight, 2)

	my_army.move_units()
	enemy_army.move_units()

	assert type(my_army.units[0]) == Lancer
	assert type(my_army.units[1]) == Healer
	assert type(my_army.units[-1]) == Warlord

	assert type(enemy_army.units[0]) == Vampire
	assert type(enemy_army.units[-1]) == Warlord
	assert type(enemy_army.units[-2]) == Knight

	#6, not 8, because only 1 Warlord per army could be
	assert len(enemy_army.units) == 6

	battle = Battle()

	assert battle.fight(my_army, enemy_army) == True
    print("Coding complete? Let's try tests!")