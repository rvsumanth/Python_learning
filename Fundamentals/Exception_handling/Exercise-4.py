''' 
The Multi-Trap List Processor
Write a function process_list(my_list, index) that takes a list and an index. 
It needs to look up the item at that index and divide the number 100 by it. 
You must write separate except blocks to handle:

IndexError (if the index is out of bounds).

TypeError (if the item at that index isn't a number).

ZeroDivisionError (if the item at that index is 0).'''



def process_list(my_list: list, index: int):
    try:
        # This will naturally throw TypeError if it's a string,
        # ZeroDivisionError if it's 0, and IndexError if out of bounds.
        result = 100 / my_list[index]
    except IndexError as e:
        print(f'Error: {e}')
    except TypeError as t:
        print(f'Type Error: {t}')
    except ZeroDivisionError as z:
        print(f'Error: {z}')
    else:
        print(f'result: {result}')

# --- Dynamic Input Parser ---
user_input = input('Enter values separated by spaces (e.g., 10 hello 0 5): ')

processed_input_list = []
for item in user_input.split():
    # If the string contains only digits, turn it into a real integer
    if item.isdigit():
        processed_input_list.append(int(item))
    else:
        # Otherwise, leave it as a raw string so it triggers the TypeError
        processed_input_list.append(item)

input_index = int(input('Enter Index value you want: '))

# Run the function
process_list(processed_input_list, input_index)