def bonus_C(salary):
    bonus = salary*0.05
    return bonus
class Employee:
    def __init__(self, name, salary):
        self.name = name
        bonus = bonus_C(salary)
        self.salary = salary+bonus
 
 
e = Employee("Sam", 15000)
print(e.name, e.salary)
 