"""it is similar to itrator but used in place return as yied so we can use lazy evalution and getting multiple return as we please """



def func(list1):
    for x in list1:
        print(x*2)
        yield x

li=[1,2,3,4,5,6,7,8,9,10]

pro=func(li)
print(next(pro))
print(next(pro))

"""lazy evalution """
def just():
    for x in range(100000000000000):
        yield x

laz=just()
print(next(laz))
print(next(laz))