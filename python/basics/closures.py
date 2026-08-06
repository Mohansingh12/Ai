"""closures are the function that remembers the values from the enclosing lexical scope even when the program flow is no longer in that 
scope"""

def multi(n):
    def number(x):
        return x * n
    
    return number

double=multi(2)
triple=multi(3)

print(double(5))
print(triple(5))