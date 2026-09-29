file =open('test.txt','w')
file.write("Hello World")
file.close()
file=open('test.txt','a')
file.write("this is a wonderfull day")
file.close()
file=open('test.txt','r')
print(file.read())
file.close()

with open('test.txt','r') as file:
    print(file.read())