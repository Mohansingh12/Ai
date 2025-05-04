# Dictionaries in Python
# are unordered collections of items. They are mutable and indexed. The items in a dictionary are stored as key-value pairs.
# A dictionary is a collection of key-value pairs

A_dictionary = {1:'mohan', 2:'ram', 3:'shyam', 4:'sita', 5:'gita'}
print(A_dictionary)

print(A_dictionary[1])
print(A_dictionary.keys)
print(A_dictionary.items())

for i in A_dictionary:
    print(i, A_dictionary[i])

print(A_dictionary.get(1))
A_dictionary[6] = 'mohan'
