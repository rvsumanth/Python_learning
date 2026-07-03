'''
program  to print the sum of odd index values of list. 
Input:[10,20,30,40,50] 
Output:60 
'''

def sum_of_odd_nums(arr: list[int]) -> int:
    if not arr:
        raise ValueError('Empty List')
    else:
        sum = 0
        for i in range(len(arr)):
            if i%2 != 0:
                sum += arr[i]
            else:
                continue
        return sum
    
x = list(map(int, input().split()))

print(sum_of_odd_nums(x))        