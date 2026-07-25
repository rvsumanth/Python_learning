'''
Move Zeroes to End
Problem: Shift all 0s to the end while maintaining the relative order of non-zero elements.
Key Intuition: Two-pointer approach. 
Pointer j tracks the position of the next non-zero element.
Iterate through the array; whenever a non-zero value is seen, swap it with arr[j] and increment j.
'''


def move_zeros(arr: list[int]) ->list[int]:
    if not arr:
        raise ValueError('Empty List')
    j = 0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[j], arr[i] = arr[i], arr[j]
            j+=1
    return arr

x =[1,0,1,2,4,0,5,7,0,78,670,0]
print(move_zeros(x))

