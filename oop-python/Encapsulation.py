""" Encapsulation Example """

class Bank_Operations_Demo:

    def __init__(self, name: str, balance = 0):
        self.name = name                        # Public Access modifier
        self._balance = balance                 # Protect Access Modifier
        self.__intrestrate = 0.3                # Private Access Modifier
        self._intrestamount = 0


    def deposite(self, amount: int) -> bool:
        ''' This is method adds amount value to the balance if amount should be greater than 0'''
        if amount > 0:
            self._balance += amount
            return True
        else:
            raise ValueError ("Invalid Amount")
        
    def withdraw(self,amount: int) -> bool:
        ''' This method substracts the amount value from the balance if 
            the amount value is greater than o and less than or equal to balance value '''
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        else:
            raise ValueError('Invalid Transaction')

    def get_balance(self) -> int:
        '''This is getter method we can get access of the balance amount value'''
        return self._balance
    
    def get_intrest(self) -> int:
        '''This method calculates intrest of the current balance value in the banck account'''
        self._intrestamount = self.__intrestrate * self._balance
        self._balance += self._intrestamount
        return self._intrestamount
    


obj = Bank_Operations_Demo('Sumanth')

deposite = obj.deposite(50000)

if deposite:
    print('Deposited')
else:
    print('Deposite Failed')

withdraw = obj.withdraw(25000)

if withdraw:
    print('Withdraw successful')
else:
    print('Withdraw failed')


Intrest_amount = obj.get_intrest()
print(f'Intrest amount: {Intrest_amount}')

Balance_amount = obj.get_balance()
print(f'Balance amount: {Balance_amount}')

        




