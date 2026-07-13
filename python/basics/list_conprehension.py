
"""""
List Comprehension is a concise way to create lists in Python. 
It allows you to generate a new list by applying an expression to each 
item in an existing iterable (like a list, tuple, or string) and optionally 
filtering items based on a condition

istead of
 for i range(len(array)):
    append(array[i] * 2)

"""

array = [1, 2, 3, 4, 5]

array= [i*2 for i in array]

