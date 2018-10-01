'''
Created on 30 Sep 2018

@author: seanv
'''
class Employee:
    def __init__(self, name, role, department, salary):
        self.name = name
        self.role = role
        self.department = department
        self.salary = salary
        
    def __repr__(self):
        print("Naam:", self.name)
        print("Role:", self.role)
        print("Department:", self.department)
        print("Jaarsalaris: {0}K".format(int((self.salary * 12)/1000)))


class Manager(Employee):

    def __init__(self, name, role, department, salary, bonus):
        self.name = name
        self.role = role
        self.department = department
        self.salary = salary
        self.bonus = (bonus/100)*salary
        
    def __repr__(self):
        print("Naam:", self.name)
        print("Role:", self.role)
        print("Department:", self.department)
        print("Jaarsalaris: {0}K".format(int((self.bonus + self.salary * 12 )/1000)))

employee = Employee("Sean", "Niks", "Niks", 22500)
employee.__repr__()

employee1 = Employee("Daan", "Niks", "Niks", 22500)
employee1.__repr__()

manager = Manager("Sean", "Niks", "Niks", 22500, 5)
manager.__repr__()

manager1 = Manager("Daan", "Niks", "Niks", 22500, 5)
manager1.__repr__()