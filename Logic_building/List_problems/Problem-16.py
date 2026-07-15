'''
Program to print the minimum element in the list. 
input:[1,2,3,4,9,11,6,7] 
output:2
'''

def minimum_element(arr:list[int]) -> int:
    if not arr:
        raise ValueError('Empty List')
    else:
        min = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < min:
                min = arr[i]
        return min

x = list(map(int, input().split()))
print(minimum_element(x))