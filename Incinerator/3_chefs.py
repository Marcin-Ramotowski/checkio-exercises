#!/usr/bin/env checkio --domain=py run 3-chefs

# You are the owner of a cafe where 3 chefs work: a JapaneseCook, RussianCook and ItalianCook. Each of them can prepare the national food and beverage:
# - JapaneseCook: Sushi and Tea;
# - RussianCook: Dumplings and Compote;
# - ItalianCook: Pizza and Juice.
# Your task is to create 3 different subclasses (one for each chef) which are the children of an AbstractCook and have these methods:
# - add_food(food_amount, food_price), which add to the client's order the value of the food which he had chosen;
# - add_drink(drink_amount, drink_price), which add to the client's order the value of the drink which he had chosen;
# - total(), which returns a string like: 'Foods: 150, Drinks: 50, Total: 200', and for the each chef instead of the Foods and Drinks will be the national food and drink that he’s used.
# Every client can choose only one chef.In this mission theAbstract Factorydesign pattern could help.
# 
# Example:
# client_1 = JapaneseCook()
# client_1.add_food(2, 20)
# client_1.add_drink(5, 4)
# client_1.total() == "Sushi: 40, Tea: 20, Total: 60"
# 
# client_2 = RussianCook()
# client_2.add_food(1, 40)
# client_2.add_drink(5, 20)
# client_2.total() == "Dumplings: 40, Compote: 100, Total: 140"
# 
# client_3 = ItalianCook()
# client_3.add_food(2, 20)
# client_3.add_drink(2, 10)
# client_3.total() == "Pizza: 40, Juice: 20, Total: 60"
# 
# 
# 
# All data here will be correct and you don't need to implement the value checking.
# 
# Input:Statements and expressions of the 3 chefs’ classes.
# 
# Output:The behaviour as described.
# 
# Precondition:All data is correct.
# 
# 
# END_DESC

from abc import ABC

class AbstractCook(ABC):
    order, foods, drinks = 0,0,0
    def add_food(self, food_amount, food_price):
        food = food_amount * food_price
        self.foods += food
        self.order += food
    def add_drink(self, drink_amount, drink_price):
        drink = drink_amount * drink_price
        self.drinks += drink_amount * drink_price
        self.order += drink

class JapaneseCook(AbstractCook):
    def total(self):
        return f"Sushi: {self.foods}, Tea: {self.drinks}, Total: {self.order}"

class RussianCook(AbstractCook):
    def total(self):
        return f"Dumplings: {self.foods}, Compote: {self.drinks}, Total: {self.order}"

class ItalianCook(AbstractCook):
    def total(self):
        return f"Pizza: {self.foods}, Juice: {self.drinks}, Total: {self.order}"