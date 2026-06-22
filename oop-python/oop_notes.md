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

## Encapsulation
- Encapsulation is the process bo binding class attributes and methods into a single unit and restrict the direct access of it.
- It hides the internal logic by providing secure accessability of class members
- **Why we use Encapsulation**
  - To protect data from unintended access or modification.
  - To hide complexity and show only essential features.
  - To provide controlled access through methods.
  - To organise code better.
- We can achieve encapsulation through "Access Modifiers"
- Access Modifiers are the responsible for restricting the direct access of class members.
- There are three types of access modifiers
  - **Public**: Public access modifier makes Class members can be accessible from anywhere like inside or outside of the class.
    - Syntax: self.<Variable_name>
  - **Protect**: Protect access modifier makes Class members can be accessible only in Class and its subclasses.
    - Syntax: "self._<variable_name>" or "def _<method_name>()"
    - Uses single underscore in front of varible name or method name that represents Protect members
  - **Private**: Priivate access modifier makes Class members can be accessible only within the class.
    - Syntax: "self.__<variable_name>" or "def __<method_name>()"
    - Uses double underscore in front of varible name or method name that represents Private members
- To acess the data we need to use getters and setters.
- Getters and Setters are the Methods which provides controlled access of private and protected members.
- We can use getters and setters in 2 ways
  - Casual Methods Getter and Setter [Example code](./Encapsulation.py)
  - Using @property and @<property_name>.setter [Example code](./Getters_Setters.py)
  
[Reference code](Encapsulation.py)

## Inheritance
- In Object oriented programming Inheritance is one of the major pillar
- Inheritance is a feature of OOP where a class is allowed to inherit the properties and behaviours (variables and methods) of another class.
- [Example code](Inheritance.py)
- Types of Inheritance 
  - Single level Inheritance - [Example code](SingleInheritance.py)
  - Multilevel Inheritance - [Example code](Multilevel_Inheritance.py)
  - Multiple Inheritance - [Example code](Multiple_Inheritance.py)
  - Hirearchical Inheritance - [Example code](Hierarchical_Inheritance.py)
  - Hybrid Inheritance - [Example code](Hybrid_Inheritance.py)
- **Why Inheritance**
  - Code Reusability: You don’t need to rewrite the same code in multiple classes. 
  - Avoid Duplication: Common code stays in the parent class
  - Improves Maintainance: Changes in one place affect all related classes.
  - Allows Extensibility: You can add new features without modifying old code. 
  - Supports porlymorphism: You can treat child classes as the parent class type (useful in large systems).
- **Diagrams**
```
Single Inheritance:

    class A 
       │ 
    class B 
```
```
Multilevel Inheritance:

    Class A 
       │
    Class B
       │
    Class C
    
```

```
Multiple Inheritance:
    A   B 
     \ / 
      C
```
```
Hierarchical Inheritance:
      A 
     / \ 
    B   C 

```
```
Hybrid Inheritance:
      A 
     / \ 
    B   C 
     \ / 
      D 
```
- **Super()**:
  -  super() is a built-in Python function that gives you access to methods and properties of the parent class from inside the child class. 
  -  It is mostly used to: 
     - Call a method from the parent class.
     - Call the parent class’s __init__() constructor. 
   -  Syntax of super() : "super().method_name()" 