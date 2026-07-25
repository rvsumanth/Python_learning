'''
Find the Second Largest Element without Sorting
Problem: Find the second largest distinct element in an O(N) single pass.
Key Intuition: Maintain two variables, largest and second_largest. 
Update second_largest when you find a new maximum or a number strictly between largest and second_largest.
'''

def second_largest_element(arr: list[int]) -> int:
    first = second = float('-inf')
    for num in arr:
        if num > first:
             second = first
             first = num
        elif num < second and num != first:
            second = num
    return second if second != float('-inf') else -1

arr = [1,2,3,4,5,23,23423]

result = second_largest_element(arr)
if result != -1:
    print(f'Second Largest Element: {result}')
else:
    print('No element')