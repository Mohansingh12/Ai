"""this is about warps that conserve the meta data of the original function"""
from functools import wraps

def body(_base_function):
    @wraps(_base_function)
    def inner_body(*args, **kwargs):
        print("this is inner body")
        _base_function(*args, **kwargs)
    return inner_body

@body
def func_1():
    """this is test for docstring"""
    print("this is func_1")


print(func_1.__name__)
print(func_1.__doc__)