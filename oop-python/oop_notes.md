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
  
## Polymorphism
- Polymorphism means “many forms”. 
- In Object-Oriented Programming (OOP), it means one interface or method behaves differently based on the object that is calling it
- There are two types: 
  - Compile-Time Polymorphism (Static) → Method Overloading 
  - Run-Time Polymorphism (Dynamic) → Method Overriding 
- **Why Do We Use Polymorphism?** 
  - Code Reusability: You don’t have to rewrite code for similar behaviors. 
  - Flexibility & Extensibility: Code can work with different types of objects. 
  - Maintainability: You can change parts of code without breaking the rest. 
  - Abstraction: Focus on "what" needs to be done, not "how" exactly it’s done. 
   - Interface Implementation: It enables powerful designs like plugin systems, APIs, and polymorphic containers.
 - **Where Do We Use Polymorphism?**
   - GUI toolkits (e.g., a draw() method works differently on Circle, Square, etc.) 
   - Machine Learning Pipelines (e.g., fit() and predict() methods) 
   - Game Development (e.g., move() works differently for Player, Enemy, NPC)
   - Web Frameworks (e.g., different controllers implementing the same method)
   - Banking Systems (e.g., calculate_interest() method works differently for SavingsAccount and FixedDeposit)
- **Method Overriding**:
  - Method Overriding occurs when a child class provides a specific implementation of a method that is already defined in its parent class. 
  - The method name, number of parameters, and return type (if applicable) must be the same. 
  - The child class’s method overrides (replaces) the parent class’s method at runtime. 
  -  The decision about which method to execute (parent or child) is made while the program is running, not at compile time.
  -  This is especially useful when using parent class references to refer to child class objects. 
-  Rules for Method Overriding:
     - Same method name: Must be same in parent and child 
    - Same number/type of parameters Must match 
    - Same return type: (Python flexible, in Java must match or be a subtype) 
    - Access modifier: Not restricted in Python, but in Java, child cannot reduce visibility
    - Inheritance required: Must be inheritance between parent and child classes 
- How overiding useful
  - Customizing behavior: You can reuse structure from a base class but customize specific behavior. 
  - Polymorphic behavior: You can write generic code using parent class but get child-specific output. 
  - Maintainable code: Changes in behavior can be done by modifying only the child class. 
  - Real-world modeling: Different objects behave differently even though the interface is the same. 
- **What is Duck Typing?** 
  - “If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.” 
  - In programming, duck typing means: 
  - An object's suitability is determined by the presence of methods and properties, rather than the actual type of the object. 
- **Why Duck Typing is Useful:**
  - Flexible & dynamic code. 
  - No need for rigid class hierarchies. 
  - Encourages polymorphism without inheritance. 
[Example code](Polymorphism.py)

## Abstraction

### What is Abstraction?
Abstraction means **showing only what is necessary** and **hiding unnecessary complexity** from the user.

The user knows **what** something does — but not **how** it does it internally.

---

### Why Do We Need Abstraction?

- Without abstraction, every class can have **different method names** for the same kind of task — causing confusion.
- No one **forces** a developer to implement required methods — bugs appear at runtime.
- The caller has to **know too much** about internal logic.

Abstraction solves all three problems.

---

### How Does Python Implement Abstraction?

Python uses the **`abc` module** (Abstract Base Class).

Two things are needed:
1. `ABC` — makes a class abstract
2. `@abstractmethod` — marks a method that **must** be implemented by every subclass

```python
from abc import ABC, abstractmethod
```

---

### Structure

```
Abstract Class  →  defines WHAT (the contract)
Concrete Class  →  defines HOW (the actual logic)
```

---

### Syntax

```python
from abc import ABC, abstractmethod

# Step 1: Create abstract class
class Animal(ABC):

    @abstractmethod
    def speak(self):   # only defined, not implemented
        pass

# Step 2: Create concrete class
class Dog(Animal):

    def speak(self):   # must implement, otherwise error
        return "Woof!"

class Cat(Animal):

    def speak(self):
        return "Meow!"

# Step 3: Use it
d = Dog()
print(d.speak())   # Woof!

c = Cat()
print(c.speak())   # Meow!
```

---

### Key Rules

| Rule | Detail |
|---|---|
| Abstract class **cannot** be instantiated | `Animal()` → ❌ TypeError |
| Subclass **must** implement all abstract methods | Otherwise → ❌ TypeError |
| Abstract class **can** have normal methods too | Not everything needs to be abstract |
| One abstract class can have **many** abstract methods | Each must be implemented in subclass |

---

### What Happens If You Break the Rules?

```python
# Rule 1: Cannot instantiate abstract class
a = Animal()       # ❌ TypeError: Can't instantiate abstract class

# Rule 2: Subclass must implement abstract method
class Bird(Animal):
    pass           # forgot to implement speak()

b = Bird()         # ❌ TypeError: Can't instantiate abstract class Bird
                   # without an implementation for abstract method 'speak'
```

Python catches these **immediately** — no hidden bugs.

---

### Abstract Class With Normal Method Too

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):       # subclass must implement this
        pass

    def description(self):   # normal method — shared by all subclasses
        return "I am a shape"

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

c = Circle()
print(c.area())           # 78.5
print(c.description())    # I am a shape  ✅ inherited normally
```

---

### Real Power of Abstraction — Common Interface

Without abstraction, different classes use **different method names** → confusion.

```python
# ❌ No abstraction — inconsistent, no contract
class Adder:
    def add(self, a, b): return a + b

class Multiplier:
    def multiply(self, a, b): return a * b   # different name!

class Subtractor:
    def subtract(self, a, b): return a - b   # different name again!
```

With abstraction, all classes follow the **same contract**:

```python
# ✅ With abstraction — consistent, enforced
from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass

class Adder(Calculator):
    def calculate(self, a, b): return a + b

class Multiplier(Calculator):
    def calculate(self, a, b): return a * b

class Subtractor(Calculator):
    def calculate(self, a, b): return a - b

# Same method name on everything
for c in [Adder(), Multiplier(), Subtractor()]:
    print(c.calculate(10, 5))
# Output:
# 15
# 50
# 5
```

---

### Abstraction vs Encapsulation (Quick Difference)

| | Abstraction | Encapsulation |
|---|---|---|
| **Hides** | Internal complexity | Internal data |
| **Purpose** | Simplify usage | Protect data |
| **Tool** | `ABC`, `@abstractmethod` | `__` (double underscore) |
| **Answers** | *What* does it do? | *Who* can access it? |

---

### Summary

| Question | Answer |
|---|---|
| **What** | Hiding complexity, showing only what is needed |
| **Why** | Consistency, enforced contracts, fewer bugs |
| **How** | `ABC` class + `@abstractmethod` decorator |
| **Who benefits** | The caller/user of the class |
| **What is hidden** | Internal logic and which class is actually running |
| **What is shown** | A simple, common method name to call |

---

### One Line to Remember

> Abstraction says: **"You know WHAT to call — you don't need to know HOW it works."**

## Abstraction in Python — Written to Kill the Confusion



### The Confusion (Read This First)

Most notes say:
> "Abstraction hides implementation details from the user"

This sounds like — the user can't see the code inside the method.

But that makes no sense because:
- The user can always **open the file and read the code**
- Even without abstraction, the user has **no idea** what happens inside `calculate()`
- So what exactly is being hidden?

**This is where every beginner gets stuck.**

---

### So What is ACTUALLY Being Hidden?

Abstraction does NOT hide code from your eyes.

It hides **which class is running** and **how that specific class works internally**
— from the part of your program that calls it.

The caller just says:
> "I don't know which class this is. I don't care.
> I just know it has `.calculate()` and it will work."

That is the real meaning of hiding in abstraction.

---

### Proof — Without Abstraction

```python
class Adder:
    def add(self, a, b):          # method called "add"
        return a + b

class Multiplier:
    def multiply(self, a, b):     # method called "multiply"
        return a * b

class Subtractor:
    def subtract(self, a, b):     # method called "subtract"
        return a - b
```

Now try to write ONE function that works with all three:

```python
def process(obj, a, b):
    return obj.???(a, b)    # what do you write here???
                            # add? multiply? subtract?
                            # you have to KNOW which class it is
                            # you have to KNOW its method name
                            # nothing is hidden — you are exposed to everything
```

You are **forced** to know the internal details of every class.
That is the opposite of abstraction.

---

### With Abstraction — The Hiding Actually Works

```python
from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass

class Adder(Calculator):
    def calculate(self, a, b):
        return a + b

class Multiplier(Calculator):
    def calculate(self, a, b):
        return a * b

class Subtractor(Calculator):
    def calculate(self, a, b):
        return a - b
```

Now write ONE function that works with all three:

```python
def process(obj, a, b):
    return obj.calculate(a, b)   # always works — no matter which class
                                 # you don't know which class it is
                                 # you don't care how it works inside
                                 # THAT is what is hidden

print(process(Adder(), 10, 5))        # 15
print(process(Multiplier(), 10, 5))   # 50
print(process(Subtractor(), 10, 5))   # 5
```

The `process()` function is completely blind to:
- Which class is passed in
- What logic runs inside
- How the result is calculated

It only knows one thing: **"it has `.calculate()` — that's enough."**

---

### Why Does This Matter in Real Projects?

Imagine you are building a payment system.

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(PaymentMethod):
    def pay(self, amount):
        # connects to NPCI
        # validates UPI ID
        # debits bank account
        # 100 lines of logic
        print(f"Paid ₹{amount} via UPI")

class CreditCard(PaymentMethod):
    def pay(self, amount):
        # validates card number
        # checks CVV
        # contacts card network
        # 100 lines of logic
        print(f"Paid ₹{amount} via Credit Card")

class NetBanking(PaymentMethod):
    def pay(self, amount):
        # redirects to bank portal
        # session handling
        # 100 lines of logic
        print(f"Paid ₹{amount} via Net Banking")
```

Now the checkout function:

```python
def checkout(payment_method: PaymentMethod, amount):
    payment_method.pay(amount)     # one line
                                   # does NOT know if it's UPI, card, or bank
                                   # does NOT know any of the 100 lines inside
                                   # completely hidden from this function

checkout(UPI(), 999)
checkout(CreditCard(), 1499)
checkout(NetBanking(), 299)
```

Tomorrow if you add PhonePe, GPay, Crypto — 
`checkout()` does not change even by one character.
Because the complexity is hidden behind `.pay()`.

---

### The Contract — The Most Important Idea

`@abstractmethod` does one job:

> It forces every subclass to implement the method.
> If they don't — Python throws an error immediately.

```python
class Divider(Calculator):
    pass                  # forgot to implement calculate()

d = Divider()
# ❌ TypeError: Can't instantiate abstract class Divider
#    without an implementation for abstract method 'calculate'
```

This is a **contract**.
Abstract class says:
> "If you inherit from me, you MUST implement these methods. No exceptions."

Without this contract — a developer can forget to implement a method
and the bug only appears at runtime when someone actually calls it.
With abstraction — Python catches it the moment you try to create the object.

---

### Full Picture — What Abstraction Actually Does

| What it does | How |
|---|---|
| Hides **which class** is running | caller only sees the abstract type |
| Hides **internal logic** of each class | caller only uses the method name |
| **Enforces** that every class has the method | `@abstractmethod` throws error if missing |
| Gives a **common interface** to all subclasses | same method name across all classes |
| Makes code work **without knowing specifics** | `process(obj)` works for any subclass |

---

### What Abstraction Does NOT Mean

| Wrong belief | Correct understanding |
|---|---|
| "User can't see the code" | User can open the file — that's not the point |
| "Implementation is invisible" | Implementation exists — caller just doesn't depend on it |
| "It's just about @abstractmethod" | It's about designing a contract + common interface |
| "Hiding = deleting information" | Hiding = the caller does not need to know or care |

---

## One Paragraph to Remember

> Abstraction means the caller does not need to know which class is running
> or how it works internally. It only knows the method name from the contract.
> The abstract class enforces that contract — every subclass must implement
> the required methods or Python immediately throws an error.
> This keeps the caller simple, consistent, and completely independent
> of internal complexity.

---

## One Line to Remember

> **"You know WHAT to call. You don't know WHICH class runs it. You don't care HOW. That is abstraction."**


 

