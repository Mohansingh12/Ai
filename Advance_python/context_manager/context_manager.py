"""context manager is for creating simple way to reduce error and handling exception in file handle and database as well"""
""" class base approch withopen using __open__ and __close__ in the background"""
from contextlib import contextmanager

with open ('test.txt', 'w') as f:
    f.write('hello world')
with open ('test.txt', 'r') as f:
    print(f.read())

with open('text2.txt', 'w') as g:
    g.write(' how are you')

""" nested context manager"""
with open ('test.txt', 'a') as f, open('text2.txt', 'r') as g:
    f.write(g.read())

with open ('test.txt', 'r') as f:
    print(f.read())

""" genrated based context manager"""
@contextmanager
def new_context(filename:str,mode:str):
    F=open(filename,mode)
    try:
        yield F
    finally:
        F.close()
with new_context('test.txt', 'r') as F:
    print(F.read())

