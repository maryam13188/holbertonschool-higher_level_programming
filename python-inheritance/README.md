# Python Inheritance Project


## Project Description


This project focuses on understanding **inheritance** in Python. By the end of the project, you should be able to explain concepts like:


- Superclass, base class, or parent class
- Subclass
- How to list all attributes and methods of a class or instance
- When instances can have new attributes
- How to inherit from another class
- How to define a class with multiple base classes
- The default class every class inherits from
- How to override a method or attribute inherited from a base class
- Attributes or methods available to subclasses through inheritance
- The purpose of inheritance
- How and when to use `isinstance`, `issubclass`, `type`, and `super`


## Requirements


- Python 3.8.5, Ubuntu 20.04 LTS
- All scripts must be executable and follow **pycodestyle 2.7**
- Each module, class, and function must have documentation explaining its purpose
- All test files should be placed inside the `tests` folder and executed using `doctest`


## Tasks


### 0. Lookup


- Create a function `lookup(obj)` that returns a list of available attributes and methods of `obj`.
- Example usage:


```python
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup


class MyClass:
    pass


print(lookup(MyClass))

The function should not use any imports.

Author

Maryam
