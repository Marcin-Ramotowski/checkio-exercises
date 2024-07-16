#!/usr/bin/env checkio --domain=py run army-units

# You are the developer of the new strategy game and you need to add the soldier creation process to it. Let's start with the 2 types - AsianArmy and EuropeanArmy (each of them will be a subclass of the Army - class with the methods for the creation of soldiers). Also there will be 3 types of soldiers in the game - Swordsman, Lancer, and Archer (also the classes). Each army has unique names for those 3 types. For the EuropeanArmy there are: Knight (for Swordsman), Raubritter (for Lancer), and Ranger (for Archer). For the AsianArmy: Samurai (for Swordsman), Ronin (for Lancer), and Shinobi (for Archer).
# Each army can create all 3 types of the soldiers using the next methods:
# 
# train_swordsman(name) - create an instance of the Swordsman.
# train_lancer(name) - create an instance of the Lancer.
# train_archer(name) - create an instance of the Archer.
# 
# All 3 classes (Swordsman, Lancer, and Archer) should have theintroduce()method, which returns the string that describes the soldiers in the following format:
# "'type' 'name', 'army type' 'specialization(basic class)'", for example:
# "Raubritter Harold, European lancer"
# "Shinobi Kirigae, Asian archer"
# 
# In this mission you should use theAbstract Factorydesign pattern.
# 
# Example:
# my_army = EuropeanArmy()
# enemy_army = AsianArmy()
# 
# soldier_1 = my_army.train_swordsman("Jaks")
# soldier_2 = my_army.train_lancer("Harold")
# soldier_3 = my_army.train_archer("Robin")
# 
# soldier_4 = enemy_army.train_swordsman("Kishimoto")
# soldier_5 = enemy_army.train_lancer("Ayabusa")
# soldier_6 = enemy_army.train_archer("Kirigae")
# 
# soldier_1.introduce() == "Knight Jaks, European swordsman"
# soldier_2.introduce() == "Raubritter Harold, European lancer"
# soldier_3.introduce() == "Ranger Robin, European archer"
#     
# soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
# soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
# soldier_6.introduce() == "Shinobi Kirigae, Asian archer"
# 
# 
# Input:The names of the soldiers and class methods.
# 
# Output:The description of soldiers.
# 
# Precondition:2 types of the army.
# 3 categories of soldiers.
# 
# 
# END_DESC

class Army():
    def train_swordsman(self,name):
        return Swordsman(self.types[0], name, self.army)

    def train_lancer(self,name):
        return Lancer(self.types[1], name, self.army)
    
    def train_archer(self,name):
        return Archer(self.types[2], name, self.army)


class EuropeanArmy(Army):
    army = 'European'
    types = ['Knight','Raubritter','Ranger']


class AsianArmy(Army):
    army = 'Asian'
    types = ['Samurai','Ronin', 'Shinobi']


class Swordsman():
    def __init__(self,type,name,army) -> None:
        self.type = type
        self.name = name
        self.army = army
    def introduce(self) -> str:
        return f"{self.type} {self.name}, {self.army} swordsman"


class Lancer():
    def __init__(self,type,name,army) -> None:
        self.type = type
        self.name = name
        self.army = army
    def introduce(self) -> str:
        return f"{self.type} {self.name}, {self.army} lancer"


class Archer():
    def __init__(self,type,name,army) -> None:
        self.type = type
        self.name = name
        self.army = army
    def introduce(self) -> str:
        return f"{self.type} {self.name}, {self.army} archer"