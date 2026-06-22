'''
Hierarchical Inheritance

A class is inherited by multiple class is known as Hierarchical Inheritance
'''

class Employee:
    def work(self):
        return 'Working in Company'

class Hr(Employee):
    pass

class Developer(Employee):
    pass

x = Hr()
y = Developer()

print(x.work())
print(y.work())