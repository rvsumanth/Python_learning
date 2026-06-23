class Company:
    def working(self):
        print('Many Employees are working in this company')

class Developer(Company):
    def working(self):
        print('Im Developer woking as an employee in this company')

class HR(Company):
    def working(self):
        print('Im HR working as an employee in this company')

class Tester(Company):
    def working(self):
        print('Im Tester Working as an employee in this company')

def workers(obj: Company):
    obj.working()

workers(Company())
workers(HR())
workers(Developer())
workers(Tester())
