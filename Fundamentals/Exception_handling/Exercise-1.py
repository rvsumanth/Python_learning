'''
The Safe Divider
Write a function safe_divide(a, b) that divides a by b. 
Use a try...except block to catch ZeroDivisionError. 
If it happens, print an error message and return None.
'''

def safe_divide(a: int,b: int) -> float:
    try:
        res = a/b
    except ZeroDivisionError as e:
        print(f'Error: {e}')
        return None
    else:
        return res

a = int(input())
b = int(input())

print(safe_divide(a,b))