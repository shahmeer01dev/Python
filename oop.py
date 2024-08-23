# CLASSES

""" A class in Python is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. Classes help in organizing code and creating reusable components. """

""" To define a class in Python, you use the class keyword followed by the class name and a colon. Here’s a simple example: """

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

""" In this example, Car is a class with an __init__ method (constructor) and a display_info method. """

# Creating Objects

""" Objects are instances of a class. You create an object by calling the class as if it were a function: """

my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()  # Output: 2020 Toyota Corolla

# Applications of Classes 

""" 
 -> Encapsulation: Bundling data and methods that operate on the data within one unit.
 -> Inheritance: Creating a new class from an existing class to reuse code.
 -> Polymorphism: Using a unified interface to operate on different data types.
 -> Abstraction: Hiding complex implementation details and exposing only the necessary parts.
"""

# Functionalities and Methods

"""
 -> Instance Methods: Operate on an instance of the class. They can access and modify the object’s attributes.
 Require a class instance and can access the instance through self:
""" 

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy")
my_dog.bark()  # Output: Buddy says woof!


"""
 -> Class Methods: Operate on the class itself rather than on instances. Defined using the @classmethod decorator.
 @classmethod decorator and take cls as the first parameter.
"""

class Animal:
    species = "Canine"

    @classmethod
    def get_species(cls):
        return cls.species

print(Animal.get_species())  # Output: Canine


"""
 -> Static Methods: Do not operate on an instance or the class. Defined using the @staticmethod decorator.
 Use the @staticmethod decorator and do not take self or cls as the first parameter.
"""

class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(5, 3))  # Output: 8

# CONSTRUCTOR & DESTRUCTOR

# Constructor

""" The constructor is a special method in Python classes that gets called when an object of a class is created. It initializes the attributes of the object. """

class Person:
    def __init__(self, name, age):
        self.name = name

# Destructor

""" The destructor is a special method in Python classes that gets called when an object of a class is destroyed. It is used to perform cleanup tasks or free up any resources. """

class Animal:
    def __init__(self):
        print("Animal created")

# Inheritance

""" Fundamental concept in object-oriented programming (OOP) that allows a class to inherit attributes and methods from another class. This helps in code reusability and the creation of a hierarchical relationship between classes. """

# Types of Inheritance

# 1. Single Inheritance = In single inheritance, a child class inherits from a single parent class.

class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Parent Name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"Child Name: {self.name}, Age: {self.age}")

# Creating an object of the Child class
child = Child("Alice", 10)
child.display()
child.show()

# 2. Multiple Inheritance = In multiple inheritance, a child class inherits from more than one parent class.

class Father:
    def __init__(self, father_name):
        self.father_name = father_name

class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.child_name = child_name

    def display(self):
        print(f"Father: {self.father_name}, Mother: {self.mother_name}, Child: {self.child_name}")

# Creating an object of the Child class
child = Child("John", "Jane", "Alice")
child.display()

# 3. Multilevel Inheritance = A class inherits from a child class, which in turn inherits from another parent class.

class Grandparent:
    def __init__(self, grandparent_name):
        self.grandparent_name = grandparent_name

class Parent(Grandparent):
    def __init__(self, grandparent_name, parent_name):
        super().__init__(grandparent_name)
        self.parent_name = parent_name

class Child(Parent):
    def __init__(self, grandparent_name, parent_name, child_name):
        super().__init__(grandparent_name, parent_name)
        self.child_name = child_name

    def display(self):
        print(f"Grandparent: {self.grandparent_name}, Parent: {self.parent_name}, Child: {self.child_name}")

# Creating an object of the Child class
child = Child("George", "John", "Alice")
child.display()

# 4. Hierarachical Inheritance = In hierarchical inheritance, multiple child classes inherit from a single parent class.

class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Parent Name: {self.name}")

class Child1(Parent):
    def show(self):
        print(f"Child1 Name: {self.name}")

class Child2(Parent):
    def show(self):
        print(f"Child2 Name: {self.name}")

# Creating objects of Child1 and Child2 classes
child1 = Child1("Alice")
child2 = Child2("Bob")
child1.display()
child1.show()
child2.display()
child2.show()

# 5. Hybrid Inheritance = Combination of two or more types of inheritance. It can be a mix of single, multiple, multilevel, or hierarchical inheritance.

class Base:
    def __init__(self, base_name):
        self.base_name = base_name

class Derived1(Base):
    def __init__(self, base_name, derived1_name):
        super().__init__(base_name)
        self.derived1_name = derived1_name

class Derived2(Base):
    def __init__(self, base_name, derived2_name):
        super().__init__(base_name)
        self.derived2_name = derived2_name

class Derived3(Derived1, Derived2):
    def __init__(self, base_name, derived1_name, derived2_name, derived3_name):
        Derived1.__init__(self, base_name, derived1_name)
        Derived2.__init__(self, base_name, derived2_name)
        self.derived3_name = derived3_name

    def display(self):
        print(f"Base: {self.base_name}, Derived1: {self.derived1_name}, Derived2: {self.derived2_name}, Derived3: {self.derived3_name}")

# Creating an object of the Derived3 class
derived3 = Derived3("Base", "Derived1", "Derived2", "Derived3")
derived3.display()

class parent1:
    def __init__(self, name):
        self.name = name
        print("parent1 constructor called")

class parent2:
    def __init__(self, age):
        self.age = age
        print("parent2 constructor called")

class child(parent1, parent2):
    def show(self):
        print("child constructor called")
        print("Name:", self.name)
        print("Age:", self.age)

c1 = child("c1_name", 24 )

print(c1)

# POLYMORPHISM

""" Polymorphism in Python is a fundamental concept in object-oriented programming that allows methods, functions, or operators to operate on different types of objects. The term “polymorphism” means “many forms,” and it enables a single interface to be used for different data types. """

# Types of Polymorphism

# Compile-Time Polymorphism (Static Polymorphism):
# Achieved through method overloading and operator overloading.

print(len("Python"))  # Output: 6
print(len([1, 2, 3, 4]))  # Output: 4
print(len({"name": "Alice", "age": 25}))  # Output: 2

# Example: The + operator can add two numbers or concatenate two strings.

# Addition
print(1 + 2)  # Output: 3

# Concatenation
print("Hello" + " " + "World")  # Output: Hello World

# Run-Time Polymorphism (Dynamic Polymorphism):
# Achieved through method overriding.

class Animal:
    def sound(self):
        print("This is an animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Creating objects
dog = Dog()
cat = Cat()

# Calling the sound method
dog.sound()  # Output: Bark
cat.sound()  # Output: Meow

# Example: A method in a parent class is overridden in a child class.

# ABSTRACTION

""" Abstraction in Python is a key concept in object-oriented programming (OOP) that helps in hiding the internal implementation details of a class and only exposing the necessary parts. This makes the code more modular, easier to understand, and maintain. """

# Abstraction Module

""" In Python, abstraction can be achieved using abstract classes and interfaces. Python provides the abc module to define abstract base classes (ABCs). """


# Abstract Classes and Methods

""" An abstract class is a class that cannot be instantiated and is meant to be subclassed. It can contain abstract methods, which are methods declared but contain no implementation. Subclasses of the abstract class must provide implementations for these abstract methods. 
1. Reusable code
2. Modularity
3. maintainability
4. Security """

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Creating objects
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow

# Functionalities and Methods

""" 
 -> Abstract Methods: Methods declared in an abstract class using the @abstractmethod decorator. These methods must be implemented by any subclass.
 -> Concrete Methods: Methods in an abstract class that have an implementation. Subclasses can use these methods directly or override them.
"""

# Types of Abstraction

""" 
 -> Data Abstraction: Hiding the details of data implementation.
 -> Control Abstraction: Hiding the details of control flow implementation.
"""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

# Creating an object
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300
