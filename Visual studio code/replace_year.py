'''
p = input()
p=p.split(" ")
for i in range(len(p)):
    if 'ear' == p[i]:
        p[i]=p[i].replace('ear','year')
ans=" "
print(ans.join(p))   //replace ear to year
'''
'''
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
 '''

#zoho - a1b5c7 - abbbbbccccccc
p = input()
for i in range(len(p)):
    if(p[i].isnumeric()):
        print(p[i-1]*int(p[i]),end="")

        