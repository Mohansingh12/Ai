"""it is very usefull in api and stuff we can use this to tell system that this is the only valid strings or numbers"""
from typeguard import typechecked
from typing import Literal

@typechecked
def testing(a: Literal['user', 'system','admin'] ) :
    return a

testing('user')
testing('system')

