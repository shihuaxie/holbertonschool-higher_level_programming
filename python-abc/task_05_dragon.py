#!/usr/bin/env python3
"""Nameless Module SwimMixin and FlyMixin"""


class SwimMixin:
    """Mixin providing swimming ability."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying ability."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim, fly, and roar."""
    def roar(self):
        print("The dragon roars!")
