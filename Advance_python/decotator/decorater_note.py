""" decorator is a python conecpt where u can preprocess function or class """

def great(base_func):
    def enhance():
        print("hello")
        base_func()
    return enhance

def func():
    print("sir")


new=great(func)
new()
"""Another way to use decorator is just adding function name before the base function"""
@great
def another_base():
     print("this time second function")
another_base()

"""function with parameters"""
def enhancer(the_base):
    def enhancement(*args, **kwargs):
        print("this code is enhanced for both codes")
        the_base(*args, **kwargs)
    return enhancement

@enhancer
def func_1():
    print("this is a simple function")

@enhancer
def func_2(first,second):
    print(first,second)

func_1()
func_2('mohan',2)

def decorator_with_args(decorator_arg1,decorator_arg2):
    def decorator(the_base):
        def enhancement(*args, **kwargs):
            print("this code is enhanced for both codes")
            print(f"decorator args are {decorator_arg1} and {decorator_arg2}")
            the_base(*args, **kwargs)
        return enhancement
    return decorator