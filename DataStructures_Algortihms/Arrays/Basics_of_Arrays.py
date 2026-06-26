import array as arr

# Creating array

x = arr.array('i',[1,2,3,4,5])
print(*x)

'''Operations'''

# Inserting
x.insert(0,0)
print('After Insert operation:',*x)

# Appending
x.append(6)
print('After append operation:',*x)

# Removing Element
x.remove(4)             # Removes the specified element at its first occurance
print('After remove operation',*x)

# Pop Operation
x.pop()                 # Removes the last element by default
print('After pop operation without arguments:', *x)

x.pop(0)                # Removes 0th indexed element from the array
print('Pop operation with argument',*x)

# Accessing elements
print(x[0])             # Accessing 1st element of array

# Slicing operations
print(*x[0:3])           # Accessing elements from 0 index to 2nd index in array

print(*x[0:])            # Accessing elements from 0 index to last index in array

print(*x[:4])            # Accessing elements from starting index to 4th index in array

print(*x[::-1])          # Prints the elements reverse

print(*x[0:4:2])

print(*x[:])