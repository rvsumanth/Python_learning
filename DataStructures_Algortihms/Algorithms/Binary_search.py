'''
Binary Search Algorithm
Divide the search space into two halves by finding the middle index "mid". 
Compare the middle of the search space with the key. 
If the key is found at middle, the process is terminated.
If the key is not found at middle, choose which half will be used as the next search space.
-> If the key is smaller than the middle, then the left side is used for next search.
-> If the key is larger than the middle, then the right side is used for next search.
This process is continued until the key is found or the total search space is exhausted.
'''

def binary_search(arr: list[int], target: int) -> int:
    '''
    input: array and target element to search in array
    output: Index of the element 
    '''

    if not arr:
        return -1
    else:
        sorted_array = arr.sort()
        low = 0
        high = len(arr)-1

        while low<=high:
            mid = low + (high-low)//2

            if sorted_array[mid] == target:
                return mid

            elif sorted_array[mid] < target:
                low = mid+1

            else:
                high = mid - 1
        return -1


arr = [1,3,4,6,237873,32987,238]
target = 237873

result = binary_search(arr, target)

if result == -1:
    print('Not found')

else:
    print(f"target element Founded at Postion: {result}")
