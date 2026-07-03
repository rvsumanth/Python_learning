'''
program to print the output as follow 
Input : [123,45,87,23,98,67] 
Output: 33

'''

def sum_of_last_element(arr: list) -> int:
    if not arr:
        raise ValueError('Empty List')
    
    else:
        try:
            sum = 0
            for i in range(len(arr)):
                sum += (arr[i])%10
                
        except Exception as e:
            print(f'Error {e}')
        else:
            return sum


x = list(map(int, input().split()))

print(sum_of_last_element(x))