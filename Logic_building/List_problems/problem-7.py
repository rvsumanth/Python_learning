'''
program to print the reverse of individual elements of list. 
 Input:[23,45,56,67] 
 Output:[32,54,65,76]
'''
# without using any python builtin function
def reverse_elements_list(arr: list) -> list:
    if not arr:
        raise ValueError('Empty list')
    
    for i in range(len(arr)):
        n = arr[i]
        # temp = n
        rev_num = 0
        while n:
            digit = n%10
            rev_num = (rev_num*10)+digit
            n //= 10

        arr[i] = rev_num

    return arr


# Using Python Builtin function( Slicing )
def reverse_elements_list_v1(arr: list) -> list:
    if not arr:
        raise(ValueError)
    for i in arr:
        i = str(i)[::-1]
    return arr




# Demonstration
x = list(map(int, input().split()))
lis = [reverse_elements_list(x), reverse_elements_list_v1(x)]
for i in lis:
    print(i)


