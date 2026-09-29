"""map is fuction for create a impletmentation of a lambda fuction and it return a instance of the map"""
from functools import reduce

list1=[1,5,21,5]
list2=['a','b','c','d']
resut=map(lambda x: x*2,list1)
print(list(resut))

"""filter create a function that filter a list"""
resut=filter(lambda x: x%2==0,list1)
print(list(resut))

"""reduce combine all the elements acording to the give fuction"""

resut = reduce(lambda x,y: x+y,list1)
print(resut)


"""zip is  function that create a function that zip two lists"""
resut = zip(list1,list2)
print(list(resut))

"""enumerate create a function that enumerate all the elements acording to the give fuction"""
for i, name in enumerate(list2):
    print(i, list2[i])

"""any is fucntion that check if there is any value that satisfy the condition"""
resut = any(x%2==0 for x in list1)
print(resut)

"""all is fuction that check if all value that satisfy the condition"""
resut = all(list1[i]%2==0 for i in list1)
print(resut)