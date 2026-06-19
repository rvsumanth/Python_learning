# Object Oriented Programming - Python
## Introduction
## Features
## Advantages and Disadvantages
## Class and Objects
## Constructor
- Constructor is a Special Method ("__init__()") that which is used to create the Objects for a class.
- Thats why it is called as a constructor, It constructs the objects.
- It also Initialises the variables for an Object.
- Constuctors can be created in two ways with parameters and without parameters.
- the constructor With parameters is known as Parameterized constructors.
- this special method invokes automatically at the time of object is going to created.
- [Reference code](./Constuctor.py).

## Instance Variables and Methods
### Instance Variables:
- Instance variables are a kind of variables that usually stores the Object data.
- Instance variables are different to each of object.
- Instance Variables are created while initializing the object
- "__init__" function is responsible for creating instance variables
- Instance varibles can be accessed though object reference and class name reference.

### Instance Methods:
- Instance methods are kind of methods that usually operates on Instance variables.
- Instance variables takes "self" as their first parameter.
- Instance variables can be accessed through object reference and class reference.

[Reference code](./Instance_variables_methods.py)

## Class Variables and Methods
### Class Variables
- Class variables are the type of variables that stores the Class level data
- Class Variables are same for all objects which are created from the class
- We can access class variables without creating object through '<class_name>.<variable_name>'
- If we change the data in class varibles it reflect on all the objects which are created from the class.

### Class Methods
- Class Methods are a type of methods which will operates on class level data without being created objects of a class
- Class methods takes cls as its first argument
- We need to use @classmethod decorator to define a class method
- We can access class methods using Class name 
```
Syntax:  <class_name>.<method_name>()
```

[Reference code](./Class_variables_methods.py)
