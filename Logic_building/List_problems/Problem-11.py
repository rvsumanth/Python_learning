'''
Program to print the output as follows. 
Input: [123,45,87,23,98,66] 
Output : 23 
Explanation: reverse the sum of last digit of each element. 
'''

def reverse_sum_elements(arr: list[int]) -> int:
    if not arr: 
        raise ValueError('Empty List')
    else:
        sum = 0
        rev_sum = 0
        for i in range(len(arr)):
            sum += arr[i]%10

        while sum:
            rev_sum = (rev_sum*10)+ sum%10
            sum//=10

        return rev_sum
    
x = list(map(int, input().split()))
print(reverse_sum_elements(x))
        