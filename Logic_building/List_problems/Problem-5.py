'''
program to print sum of even of index values of list. 
    Input:[10,20,30,40,50] 
    Output:90 
'''

def sum_of_even_nums(arr: list[int]) -> int:
    if not arr:
        raise ValueError('Empty List')
    sum =0
    for i in range(len(arr)):
        if i%2 == 0:
            sum += arr[i]
        else:
            continue
    return sum

x = list(map(int,input().split()))
print(sum_of_even_nums(x))