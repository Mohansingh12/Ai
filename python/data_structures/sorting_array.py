x=[1,6,3,4,5]
p=0
q=len(x)-1
for i in range(len(x)):
    if p>q:
        break
    if x[p]>x[q]:
        temp=x[p]
        x[p]=x[q]
        x[q]=temp
        print(i)
        print(p,q)
        q-=1
    else:
        p+=1
    
    
print(x)