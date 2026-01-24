class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
head=Node(1)
second=Node(2)
third=Node(3)
four=Node(4)
head.next=second
second.next=third
third.next=four
fast=head
slow=head
alist=[]
"""while fast and fast.next:
    fast=fast.next.next             #output seem to same in mention in leetcode 
                                     the thing is that here output type is in the list so it not allowing as solution 
                                     it is correct when you just return the node of particular of it , atomitically , leetcode make and 
                                     seem like a list of element but actually , when we are return the node since it is linked to beside element and where that element is connected to other element 
                                     so , i will give up to where tail become None
    slow=slow.next                       
fast=slow
while fast:
    alist.append(fast.val)
    fast=fast.next
print(alist) #"""

def middle_node():
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow
print(middle_node())
    

