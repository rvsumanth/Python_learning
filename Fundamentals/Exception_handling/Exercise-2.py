'''
The Integer Enforcer
Write a program that continuously prompts the user to enter their age using input(). 
If the user types something that isn't a whole number (like "twenty" or "15.5"), 
catch the ValueError, print a warning, and ask them again. 
The loop should only exit when a valid integer is entered.
'''



while True:
    try:
        x = input('Enter age: ')
        x = int(x)
        if x <= 0:
            raise ValueError('Age should not be zero or negative')
    except ValueError as e:
        print(f'Error - {e}')
    else:
        print('Success')
        break


