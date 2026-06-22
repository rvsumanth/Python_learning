''' 
Single Inheritance Example

One child class inherits one parent class

'''

class Employee:
    def work(self):
        return 'Working'
    
class Developer(Employee):
    def write_code(self):
        return 'Writing code'
    
x = Developer()
print(x.work())
print(x.write_code())
