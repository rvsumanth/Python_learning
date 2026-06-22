'''
Multi level inheritance 

Multi level inheritance - a class is derived from another class, which in turn is derived
from another class
simply:- Child inherits from parent, and that parent inherits from another parent. 
'''

class GrandFather:
    def house(self):
        return "Living in Grandfather's House (Inherited)"
    
class Father(GrandFather):
    def bike(self):
        return "Using Father's Bike (Inherited)"
    
class Child(Father):
    pass

x = Child()
print(x.house())
print(x.bike())