"""" So there are itrable that the list and other things we can itrate and there is itrator which itrate these structures"""

a=[1,2,3,4,5,6]

run=iter(a)
print(next(run))
print(next(run))

for i in run:
    print(i)

