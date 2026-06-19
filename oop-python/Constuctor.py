"""
Constuctor Example
"""
class ConstructorExample:
    def __init__(self):
        print(f'This is Constructor invoked while creating object here is object: {self}')
    
class PrametrizedConstructorExample:    
    def __init__(self, name: str):
        self.name = name
        print(f'This is parameteraized constructor here is your parameter: {self.name}')


constructor_obj = ConstructorExample()

param_constructor_obj = PrametrizedConstructorExample('param-1')