'''
 Key or Index?
Write a function extract_element(data, key_or_index) that works for both lists and dictionaries.

If data is a list and the index doesn't exist, handle the IndexError.

If data is a dictionary and the key doesn't exist, handle the KeyError.
In both failure cases, return a fallback string: "Element not found".
'''

def extract_elements(data, key_or_index):
    try:
        res = data[key_or_index]
    except IndexError as e:
        print(f'Error: {e}')
    except KeyError as k:
        print(f'Error: {k}')
    else:
        print(res)    


#  list
list_data = [10,20,30,49,69,30,100,20]

index = int(input('Enter an index value: '))
extract_elements(list_data, index)


# For dict
dict_data = {
    'name': 'Sumanth',
    'age' : 22,
    'address' : 'Japan',
    'salaray' : 500000,
    'role' : 'Developer'
             }

key = input('Enter a key value: ')
extract_elements(dict_data, key)







