'''
Program to print the maximum element in the list. 
input:[1,2,3,4,9,11,6,7] 
output:11
'''
def max_ele(arr: list[int]) -> int:
    if not arr:
        raise ValueError('Empty List')
    else:
        max = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max:
                max = arr[i]
        return max
    
# builtin method to find maximumm element in the list   
def builtin_max(arr: list[int]) -> int:
    if not arr:
        raise ValueError('Empty List')
    else:
        return max(arr)


x = list(map(int, input().split()))
print(max_ele(x))
print(builtin_max(x))