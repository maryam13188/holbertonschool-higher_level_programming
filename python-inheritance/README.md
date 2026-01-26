# Python Inheritance


This project contains a series of Python exercises to practice **object-oriented programming (OOP)** concepts such as **inheritance**, **subclasses**, **overriding methods**, and **data validation**.


## Learning Objectives


By the end of this project, you are expected to understand:


- What is a superclass / base class / parent class
- What is a subclass
- How to list all attributes and methods of a class or instance
- When an instance can have new attributes
- How to inherit from another class
- How to define a class with multiple base classes
- The default class every class inherits from
- How to override methods or attributes inherited from the base class
- Attributes or methods available to subclasses via inheritance
- The purpose of inheritance
- How to use `isinstance`, `issubclass`, `type`, and `super()`


## Requirements


- All Python files are compatible with Python 3.8.5+
- All files should follow PEP8 style guidelines
- All scripts are executable and start with `#!/usr/bin/python3`
- All modules, classes, and functions contain proper documentation (docstrings)


## Files


| Task | File | Description |
|------|------|-------------|
| 0    | `0-lookup.py` | Function to list available attributes and methods of an object |
| 1    | `1-my_list.py` | Class `MyList` that inherits from `list` and has a `print_sorted()` method |
| 2    | `2-is_same_class.py` | Function `is_same_class()` to check if an object is exactly an instance of a class |
| 3    | `3-is_kind_of_class.py` | Function `is_kind_of_class()` to check if an object is instance or subclass of a class |
| 4    | `4-inherits_from.py` | Function `inherits_from()` to check if an object inherits from a class |
| 5    | `5-base_geometry.py` | Empty class `BaseGeometry` |
| 6    | `6-base_geometry.py` | Class `BaseGeometry` with `area()` method that raises an exception |
| 7    | `7-base_geometry.py` | Class `BaseGeometry` with `integer_validator()` method |
| 8    | `8-rectangle.py` | Class `Rectangle` inherits from `BaseGeometry` with width and height |
| 9    | `9-rectangle.py` | Full `Rectangle` class with `area()` and `__str__()` |
| 10   | `10-square.py` | Class `Square` inherits from `Rectangle` with size |
| 11   | `11-square.py` | Class `Square` with `__str__()` returning `[Square] <size>/<size>` |


## How to Run


You can run each task using Python3:


```bash
$ python3 <task-file>.py
```
## For example:
```
$ python3 1-my_list.py
```
## Author

Maryam
