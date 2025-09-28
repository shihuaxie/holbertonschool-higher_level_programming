#!/usr/bin/env python3
""" Nameless module for FlyingFish class """


class Fish:
    """Class representing a fish with swimming ability and water habitat."""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Class representing a bird with flying ability and sky habitat."""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish that inherits from both Fish and Bird.
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(slef):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
