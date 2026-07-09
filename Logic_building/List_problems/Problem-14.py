'''
Program to print the count of prime numbers in list. 
input:[1,2,3,4,5,6,7] 
output:4 

program to print the sum of prime numbers in list 
input:[1,2,3,4,5,6,7] 
output:17

program to print the sum of non  prime numbers in list 
input:[1,2,3,4,5,6,7] 
output:11

'''
def is_prime(num: int) -> bool:
    if num <= 0 or num == 1:
        return False
    else:
       try:
            for i in range(2, int(num**0.5)+1):
                    if num % i == 0:
                        return False
                    
       except Exception as e:
           print(f'Error: {e}')

       else:
            return True

# Count of prime numbers in the list
def count_of_prime(arr: list[int]) -> int:
    if not arr :
        raise ValueError('Empty List')
    else:
        count = 0
        for i in arr:
            if is_prime(i):
                count += 1
        return count
    
# Sum of Prime numbers in the list
def sum_of_prime(arr: list[int]) -> int:
    if not arr:
        raise ValueError('Empty List')
    else:
        sum = 0
        for i in arr:
            if is_prime(i):
                sum += i
        return sum

# Sum of Non prime numbers in the list
def sum_of_non_prime(arr: list[int]) -> int:
    if not arr:
        raise ValueError('Empty List')
    else:
        sum = 0 
        for i in arr:
            if not is_prime(i):
                sum += i
        return sum


x= list(map(int, input().split()))
print(f'Total Prime numbers in the List: {count_of_prime(x)}')

print(f'Sum of Prime numbers in the list: {sum_of_prime(x)}')

print(f'Sum of Non prime numbers in the list: {sum_of_non_prime(x)}')