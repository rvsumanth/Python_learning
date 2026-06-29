'''Program to print Sum of all the elements of list'''

# def sum_elements_list(data: list) -> int:
#     if data is None:
#         raise ValueError('Invalid List')
#     else:
#         sum = 0
#         for i in data:
#             try:
#                 sum+=i
#             except (ValueError, TypeError) as e:
#                 print(f'Error{e}')
#         return sum
    
# x = input('Enter multiple numbers: ')
# lis = []
# for i in x.split():
#     try:
#         lis.append(int(i))
#     except (ValueError, TypeError) as e:
#         print(f'Error: {e}')


# print(sum_elements_list(lis)) 

def sum_elements_list(data: list) -> int:
    if data == []:
        raise ValueError('Invalid List')
    else:
        sum = 0
        for i in data:
            try:
                sum+=int(i)
            except (ValueError, TypeError) as e:
                print(f'Error{e}')
        return sum
    

x = list(input().split())

print(sum_elements_list(x))