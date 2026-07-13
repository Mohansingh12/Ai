class link:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

l1=link(0)
l1.a=link(1)
l1.b=link(2)
l1.c=link(3)

l2=link(0)
l2.a=link(4)
l2.b=link(5)
l2.c=link(6)

l1.a.next=l1.b
l1.b.next=l1.c  

l2.a.next=l2.b
l2.b.next=l2.c
head=l1.a
head2=l2.a
sum=0

while head:
    sum+=head.val
    head=head.next
    sum+=head2.val
    head2=head2.next
print(sum)
