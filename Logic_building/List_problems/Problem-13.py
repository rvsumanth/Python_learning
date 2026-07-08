'''
program to print only not   prime numbers in the list 
input:[1,2,3,4,5,6,7] 
output:[1,4,6] 
'''

def is_prime(num: int) -> bool:
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True


def prime_numbers(arr: list[int]) -> list:
    if not arr:
        raise ValueError('Empty List')
    else:
        # result =[]
        # for i in arr:
        #     if is_prime(i):
        #         result.append(i)  
        result = [i for i in arr if not is_prime(i)]             
        return result


x = list(map(int, input().split()))
print(prime_numbers(x))