#!/usr/bin/env python3

# Mixin for swimming behavior
class SwimMixin:
    def swim(self):
        print("The creature swims!")


# Mixin for flying behavior
class FlyMixin:
    def fly(self):
        print("The creature flies!")


# Dragon class inheriting both mixins
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
