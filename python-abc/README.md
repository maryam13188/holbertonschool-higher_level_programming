
# Python OOP - Advanced Concepts

## Project Description
This repository contains exercises demonstrating advanced **Object-Oriented Programming (OOP)** concepts in Python.  
The project covers:


- Abstract Classes  
- Duck Typing  
- Subclassing Iterators  
- Multiple Inheritance  
- Mixins  


Each task focuses on a specific OOP principle, helping you understand and apply Python’s OOP features in real-world scenarios.


---
## Learning Objectives:
Abstract Classes: Understand and apply abstract classes to define common interfaces while enforcing certain levels of class completeness.
Interfaces and Duck Typing: Grasp the concept of interfaces and duck typing to ensure that objects adhere to a specific contract or protocol.
Subclassing Standard Base Classes: Learn to extend standard base classes like lists, dictionaries, and iterators to create custom data structures with specialized behavior.
Method Overriding: Employ method overriding to alter or enhance the behavior of base class methods.
Multiple Inheritance: Understand and apply multiple inheritance to form complex relationships between classes.
Mixins: Utilize mixins to compose behavior across unrelated classes.

## Resources:
Python 3 Object-Oriented Programming
ABC — Abstract Base Classes
Real Python - Object-Oriented Programming (OOP) in Python 3
Corey Schafer - OOP Playlist
sentdex - Python OOP Tutorial
---


## Tasks and Files


| Task | Description | Files |
|------|-------------|-------|
| 0 – Abstract Animal | Abstract class `Animal` with abstract method `sound`. Subclasses `Dog` and `Cat` implement `sound`. | `task_00_abc.py`, `main_00_abc.py` |
| 1 – Shapes & Duck Typing | Abstract `Shape` class with `area` and `perimeter`. Concrete classes `Circle` & `Rectangle`. Function `shape_info` uses duck typing. | `task_01_duck_typing.py`, `main_01_duck_typing.py` |
| 3 – CountedIterator | Iterator subclass that tracks the number of items iterated over using `__next__` and `get_count`. | `task_03_countediterator.py`, `main_03_countediterator.py` |
| 4 – FlyingFish | Demonstrates multiple inheritance with `Fish` and `Bird` as parents of `FlyingFish`. Method overriding and MRO exploration. | `task_04_flyingfish.py`, `main_04_flyingfish.py` |
| 5 – Dragon & Mixins | Uses `SwimMixin` and `FlyMixin` to give a `Dragon` object the ability to swim, fly, and roar. | `task_05_dragon.py`, `main_05_dragon.py` |


---


## Usage Examples


### Task 0 – Abstract Animal
```python
from task_00_abc import Dog, Cat


print(Dog().sound())    # Bark
print(Cat().sound())    # Meow
```

## 📌 Key Concepts

Abstract Classes: Enforce contracts for subclasses to implement required methods.

Duck Typing: Enables polymorphism based on object behavior, not explicit inheritance.

Iterators & __next__: Allows tracking iteration progress with custom behavior.

Multiple Inheritance: Combines behaviors from multiple parent classes; understand MRO to avoid conflicts.

Mixins: Add modular, reusable functionality without deep or complex inheritance hierarchies.

## 👤 Author

Mariam Al-Essa

