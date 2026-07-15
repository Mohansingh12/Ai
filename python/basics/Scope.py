""" so The scope of a variable is the region of the program where it is defined and can be accessed. 
In Python, there are four types of variable scope:"""

a=10

def my_function():
    b=20
    print(a)  # Accessing global variable 'a'
    print(b)  # Accessing local variable 'b'

def another_function():
    c=30
    d=a+c

def yet_another_function(): 
    global a # according to my understanding this is require beacuse python will treat 'a' as a local variable if we try to modify it
             # without declaring it as global
    a+=1
    print(a)  # This will raise an UnboundLocalError because 'a' is being referenced before assignment


my_function()  # Output: 10, 20
another_function()  # This will not produce any output
yet_another_function()  # This will raise an UnboundLocalError because 'a' is being referenced before assignment