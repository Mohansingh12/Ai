"""protocol is being used for enforcing type hint for python class to have at least these functions"""



from typing import Protocol

class Animal(Protocol):
    def sound(self):
        print("I")
    def walk(self):
        print("I have")
class Dog():
    def sound(self):
        print("Bark")
    def walk(self):
        print("4 legs")
andy :Animal = Dog()
andy.sound()
