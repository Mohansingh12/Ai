"""it is used to give a option between two data types"""
from typing import Union

def testing(a: list) -> Union[int, str]:
    return a

""" also can be writen as
def testing(a: int) -> str | int :

    return a
"""

print(testing(5))