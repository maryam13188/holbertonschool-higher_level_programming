#!/usr/bin/env python3
from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Return the sound made by the animal"""
        pass


# Subclass Dog
class Dog(Animal):
    def sound(self):
        return "Bark"


# Subclass Cat
class Cat(Animal):
    def sound(self):
        return "Meow"
