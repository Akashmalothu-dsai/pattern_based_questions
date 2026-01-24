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

#detection using the hare algorithm
def start_cycle_node():
    fast=head
    slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if slow==fast:
            break
    slow=head
    while slow!=fast:
        fast=fast.next
        slow=slow.next
    return slow
print(start_cycle_node())

#deferent manner writting code 

def start_cycle():
    slow=head
    fast=head
    flag=False
    while fast and fast.next:
        slow=slow.next
        fast=fast.next if flag else fast.next.next
        if slow==fast:
            if flag :
                return slow
            else:
                flag=True
                slow=head
print(start_cycle())