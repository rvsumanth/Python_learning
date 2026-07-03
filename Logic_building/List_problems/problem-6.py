'''
program to print the list in reverse order. 
    Input:[10,20,30,40,50] 
    Output:[50,40,30,20,10]
'''
# without using python features
def list_in_reverse_order(arr: list[int]) -> list:
    if not arr:
        raise ValueError('Empty List')
    else:
        i = 0
        j = len(arr)-1
        while i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1  
        return arr
    

# Using python features
def list_in_reverese_order_v1(arr: list[int]) -> list:
    if not arr:
        raise ValueError('empty List')
    else:
      x = arr[::-1]  
      return x
    
x = list(map(int, input().split()))

y = [list_in_reverese_order_v1(x), list_in_reverse_order(x)]

for i in y:
    print(i)