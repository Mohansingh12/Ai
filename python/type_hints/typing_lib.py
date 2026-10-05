"""We these for ditemenine the output and expet type of data so thet we can create more robust solutions"""

from typing import List

a=list[int]
b=dict[int,str]
c=tuple[int,str]

"""it will throw a error if it gets any other data type"""

def add(a,b) -> int:
    return a+b

def multiply(a,b:int) -> int:
    return a*b

"""it also use to ask for spesfic return type"""

