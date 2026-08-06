"""In python we can pass multiple arguments to a function. We can also use default arguments, keyword arguments, and variable-length 
arguments."""

"""Variable number of arguments"""

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

"""Variable keyword arguments"""
def data(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
