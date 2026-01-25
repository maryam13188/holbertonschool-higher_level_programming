# Python - Classes


This project covers **Object-Oriented Programming (OOP) in Python** through creating a `Square` class with increasing complexity.


## Learning Objectives


By the end of this project, you are expected to understand and explain:


- What is **OOP**
- What is a **class**, **object**, and **instance**
- Difference between class and object/instance
- What is an **attribute** (public, protected, private)
- How to use **self**
- What is a **method** and the special `__init__` method
- Concepts of **Data Abstraction**, **Encapsulation**, and **Information Hiding**
- How to use **property**, getters, and setters in Python
- How to validate attributes and control access


## Project Tasks


| Task | Description |
|------|------------|
| 0. My first square | Create an empty `Square` class |
| 1. Square with size | Add a private `size` attribute |
| 2. Size validation | Validate `size` as integer ≥ 0 |
| 3. Area of a square | Add method `area()` to calculate the square area |
| 4. Access and update | Add getter and setter for `size` with validation |
| 5. Printing a square | Add method `my_print()` to print the square with `#` |
| 6. Coordinates | Add `position` attribute to control printing offset |


## Requirements


- Python 3.8+
- All files executable and follow `#!/usr/bin/python3` shebang
- Use **pycodestyle** for style checks
- Each class, method, and module must include **docstrings**
- No external modules should be imported


## Examples


```python
from square import Square


s = Square(3, (1, 2))
print(s.size)      # 3
print(s.position)  # (1, 2)
print(s.area())    # 9
s.my_print()

Will print:



 ###
 ###
 ###
Author

Maryam Alessa
