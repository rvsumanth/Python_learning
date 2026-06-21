class Employee:
    def __init__(self, name):
        self.name = name
        self._salary = 0

    @property                       # Getter Method for getting the salary value of employee
    def salary(self):
            return self._salary
    
    @salary.setter                  # Setter Method for Setting the new Salary value
    def salary(self, amount):
         if amount<0:
              raise ValueError('Invalid amount')
         self._salary = amount

x = Employee('Sumanth')
x.salary = 50000
print(x.salary)
     