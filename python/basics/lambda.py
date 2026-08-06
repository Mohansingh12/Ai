"""lambda funtion:- is a small anonymous function that can take any number of 
arguments, but can only have one expression. It is often used for short, 
simple functions that are not reused elsewhere in the code."""

def lam(x):
    y=lambda z: z+ z
    print(y(5))

lam(5)

y=lambda z: (z+z)*2
print(y(5))

students = [
    ("Mohan",80),
    ("Rahul",95),
    ("Ankit",70)
]

students.sort(key=lambda x:x[1])

print(students)