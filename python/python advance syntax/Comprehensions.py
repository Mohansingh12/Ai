"""comprehensions create a function that check if all values that satisfy the condition"""
from python.basics.Higher_Order_Functions import square

"""list"""

numbers = [1,2,3,4,5,6,7,8,9,10]

square=[x**2 for x in numbers]
print(square)

even = [x for x in numbers if x % 2 == 0]
print(even)

even_odd =["even" if x%2==0 else "odd" for x in numbers]
print(even_odd)

"""dictonary"""
names =["alice","bob","charlie"]

length = {x:len(x) for x in names}
print(length)

"""sets"""

numbers = [1, 2, 2, 3, 3, 4]

unique_squares = {x ** 2 for x in numbers}

print(unique_squares)

"""generator"""

numbers=(x *2 for x in range(10))
print(next(numbers))

for number in numbers:
    print(number)