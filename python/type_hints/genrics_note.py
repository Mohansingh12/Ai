"""Generics are being used for the different types of data type for the same class"""
from typing import Generic, TypeVar
T = TypeVar("T")
class test(Generic[T]) :
    def __init__(self,a: T ) :
        self.a = a
        print(a)

testing = test[int](1)

testing2= test[str]('mohan')

