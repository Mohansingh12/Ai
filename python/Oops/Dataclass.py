"""Dataclass is a Python module that provides a decorator and functions for automatically adding special methods to user-defined classes. 
It is part of the standard library and was introduced in Python 3.7. The main purpose of dataclasses is to simplify the creation of 
classes that are primarily used to store data, by automatically generating methods like __init__, __repr__, __eq__, and others based 
on the class attributes."""

from dataclasses import dataclass

@dataclass
class car:
    brand: str
    model: str
    color: str

car1=car('honda','city','white')
print(f"Brand: {car1.brand}, Model: {car1.model}, Color: {car1.color}")