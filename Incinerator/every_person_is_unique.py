#!/usr/bin/env checkio --domain=py run every-person-is-unique

# pre.example {        border: 1px solid #aaa;        border-radius: 3px;        background: #eee;        margin-left: 20px;        padding: 5px;        overflow: auto;    }    p.indent {        margin-left: 20px;    }Every year, the number of your friends is increasing and monitoring information about their lives is becoming more difficult. Let's simplify and slightly automate this process. Indeed, the simplification of routine processes is one of the key programming tasks.
# 
# You have to create a class ‘Person’ and a few methods to work with its instances. See the class description below.
# 
# classPerson(first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown')
# 
# It returns a new instance  of the ‘Person’ class  with the name and surname [first_name,last_name], date of birth -birth_date(in 'dd.mm.yyyy' format), current job -job, number of working years -working_years, average salary -salary(per month), current country and city - [country,city] and gender -gender. The gender parameter could be 'male' or 'female'. If this parameter is undefined, the default value is - 'unknown'.
# 
# 
# Person(‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’) ==
# Person(‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’)
# 
# Person(‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’) ==
# Person(‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’, ‘unknown’)
# 
# name()
# 
# Returns the full name (name and surname, separated by a whitespace).
# 
# 
# Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’).name() == ‘John Smith’
# 
# age()
# 
# Returns the person’s age - the number of fully lived years. (The current date is 01.01.2018)
# 
# 
# Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’).age() == 38
# 
# work()
# 
# Returns the person’s job in a sentence as follows:‘He is a ...’ (if male)‘She is a ...’ (if female)‘Is a ...’ (if unknown)
# 
# 
# Person (‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’).work() == ‘Is a designer’
# 
# money()
# 
# Returns an amount of money, earned during the working years. It should be returned in format xx xxx … - every 3 decimal places should be separated by a whitespace. For example:‘10 568’‘1 051 422’
# 
# 
# Person (‘John’, ‘Smith’, ‘19.09.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’).money() == ‘648 000’
# 
# home()
# 
# Returns the country and the city where a person lives:‘Lives in the city, country’
# 
# 
# Person (‘Hanna Rose’, ‘May’, ‘05.12.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’).home() == ‘Lives in Vienna, Austria’
# 
# In this mission all data will be correct and you won't need to implement the value checking.
# 
# Input:Statements and expressions that use the ‘Person’ class.
# 
# Output:The behaviour of an instance as described above.
# 
# Precondition:All data is correct.
# 
# 
# END_DESC

class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown') -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender
    def name(self):
        return ' '.join([self.first_name, self.last_name])
    def age(self):
        convert = self.birth_date.split('.')
        return 2017 - int(convert[-1]) if int(convert[0]) != 1 or int(convert[1]) != 1 else 2018 - int(convert[-1])
    def work(self):
        if self.gender =='male':
            return f"He is a {self.job}"
        elif self.gender == 'female':
            return f"She is a {self.job}"
        else:
            return f"Is a {self.job}"
    def money(self):
        score = str(int(self.working_years)*12*int(self.salary))
        score = list(score)
        x = 0
        for i in range(-3,-len(score),-3):
            score.insert(i+x,' ')
            x -= 1
        return ''.join(score)
    def home(self):
        return f"Lives in {self.city}, {self.country}"