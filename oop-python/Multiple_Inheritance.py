'''Multiple Inheritance

A class that inherits multiple classes at a time
'''

class Father:
    def chocolate(self):
        return 'Chocolate given by Father'

class Mother:
    def cooldrink(self):
        return 'Cooldrink given by Mother'
    
class Child(Father, Mother):
    pass

x = Child()
print(x.chocolate())
print(x.cooldrink())