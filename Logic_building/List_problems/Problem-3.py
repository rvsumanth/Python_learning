'''program to print odd index value of list. 
 Input:  [10,20,30,40,50] 
 Output: 10 30 50 '''

def odd_index_value(arr: list):
    if not arr:
        raise ValueError('Empty List')
    else:
        for i in range(len(arr)):
            if i%2 ==0:
                continue
            else:
                print(f'index: {i}',end =" ")
                print(f'value: {arr[i]}')


x = list(map(int, input().split()))
odd_index_value(x)
