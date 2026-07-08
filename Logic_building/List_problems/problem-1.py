'''
1.program to print list of elements one by one. 
Input:[10,20,30,40,50] 
Output:        10 
               20 
               30 
               40 
               50 
               
'''


def printing_list_elements(x: list):
    for i in x:
        print(i)
    

x = list(map(int,input('Enter values: ').split()))
printing_list_elements(x)
