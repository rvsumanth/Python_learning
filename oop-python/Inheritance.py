""" Interitence example code"""

class Account:
    def __init__(self, acc_num: str, name:str):
        self.account_number = acc_num
        self.account_name = name
        self._balance = 0

    def deposite(self, amount: int) -> bool:

        '''This Function adds the amount value to balance value
          if the amount value is greater than zero
          Inputs: Amount value (Interger)
          Output: Boolean value (return true if executed succesfully else returns False)'''
        
        if amount < 0:
            raise ValueError('Invalid amount')
        else:
            self._balance += amount
            return True
    
    def withdraw(self, amount: int) -> bool:
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True

        else:
            raise ValueError('Invalid Amount')
        
    @property
    def balance(self) -> float:
        return self._balance
    
class Savings_account(Account):
    def add_intrest(self, rate: float) -> str:
        intrest = self._balance * rate/100
        self._balance += intrest
        return f'Intrest amount: {intrest} added'
    
class Current_account(Account):
    def withdraw(self,amount: int) -> bool:
        overdraw_limit = 5000
        if amount > (self._balance + overdraw_limit):
            return ValueError('Limit Exceeded')
        else:
            self._balance -= amount
            return True



print('--'*30)
x = Savings_account('ac101', 'sumanth')
print('Deposite Successful' if x.deposite(10000) else 'Deposite falied')
print('Withdraw Successful' if x.withdraw(2000) else 'Withdraw failed')
print(x.add_intrest(0.5))
print(f'Current Balance: {x.balance}')

print('--'*30)
y = Current_account('ac102','smith')
print('Deposite Successful' if y.deposite(10000) else 'Deposite falied')
print('Withdraw Successful' if y.withdraw(2000) else 'Withdraw failed')
print(f'Current Balance: {y.balance}')

print('--'*30)





             
