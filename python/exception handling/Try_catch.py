
test=5
if type(test) != str:
    raise TypeError('test is not a string')
try:
    for i in range(len( test)):
        print(5)

except TypeError as e:
    print(e)
else:
    print('success')
finally:
    print('success')