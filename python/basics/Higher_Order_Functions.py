""" higher order functions are functions that can take other functions as arguments or return 
functions as results. """

def square(x):
    return x*x

def area(func, x):
    return func(x)*x

print(area(square, 5))

a=[3,5,3,52,5]

b=map(lambda x:x*x, a)

print(list(b))