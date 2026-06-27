''' 
Custom Banking Exceptions
Create a custom exception class named InsufficientFundsError that inherits from Exception. 
Then, write a BankAccount class with a balance attribute and a withdraw(amount) method. 
If a user tries to withdraw more money than they have, raise your custom exception and pass a helpful error string into it.'''


class InsufficientFundsError(Exception):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f'Insufficient Funds! cannot processed your requested withdraw amount {self.amount}')


class Bank:
    def __init__(self, balance: int):
        self._balance = balance

    def withdraw(self, amount: int):
        if amount < 0:
            print('Amount value must be greater than zero ')
        if amount > self._balance:
            raise InsufficientFundsError(amount)
        else:
            self._balance -= amount
            print('Success')
            

try:
    x = Bank(10000)

    x.withdraw(100000)
except InsufficientFundsError as e:
    print(f'error: {e}')