#!/usr/bin/python3
"""This is an anbstact Animal module and its subclass"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    A class Animal

    Args:
        ABC
    Returns:
        Nothing
    """
    #abcmethod decorator, it can have multiple abcmethods.
    #no implementation, only declaration
    @abstractmethod
    def sound(self):
        pass

#subclass Dog, inherits from Animal
class Dog(Animal):
    #implementing the sound method
    def sound(self):
        return ("Bark")

#subclass Cat, inherits from Animal
class Cat(Animal):
    #implementing the sound method
    def sound(self):
        return ("Meow")
