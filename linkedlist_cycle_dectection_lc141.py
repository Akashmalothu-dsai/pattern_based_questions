
class Node:
    def __init__(self,value):
        self.value=value
        self.next=next
n1=Node(1)
n2=Node(2)
n3=Node(8)
n4=Node(4)
head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n2
#using hash map concept 
avalue=head
set=[]
while avalue.value not in set:
    set.append(avalue.value)
    avalue=avalue.next
#print(avalue.value)

#using Floyd's alogrithm or tortoise or hare algorithm
def cycle_detection():
    index=[]
    fast=head
    slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if slow==fast:
            return True
    return False


    