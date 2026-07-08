'''
program to print the output as follow. 
 Input: [123,45,87,23,98,67] 
 Output : 30
 Explanation: sum of  first digit of each element in list 
'''

def sum_of_first_element(arr: list[int]) -> int:
    if not arr: 
        raise ValueError('Empty List')
    else:
        sum =0
        for i in arr:
            sum += int(str(i)[0])
        return sum
    

x = list(map(int,input().split()))
print(sum_of_first_element(x))