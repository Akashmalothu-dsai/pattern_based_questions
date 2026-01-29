n=7
#one way of approach without using the slow and fast pointer 
def happy_num(n):
    while len(str(n))!=1:
        sum=0
        for i in str(n):
            sum+=(int(i))**2
        n=sum
    return n==1 or n==7#in this example we know the happy number ie 1, 7 among the number from 1 to 9 
print(happy_num(n))#seven also the happy number due to repeatly sum of square of digit rom the 7 we get at moment get a number is 1
 
"""
#by using concept of the slow and fast pointer #this not optimised because repeatdly call of next_num function
def happy_number(n):
    def next_num(x):
        sum=0
        while x>0:
            x,r= divmod(x,10)
            sum+=r**2
        return sum
    slow=n
    fast=next_num(n)
    while fast!=1 and slow!=fast:#this will stop at fast equal to 1 and the single digit 
        slow=next_num(n)
        fast=next_num(next_num(n))
    return fast==1
print(happy_number(n))"""

#depends on the cycle concept (optimised time compecticity big of lenght of number )
def happy_numbers(n):
    seen=set()
    while n!=1:
        if n in seen:
            return False
        seen.add(n)
        sum=0
        for i in str(n):
            sum+=int(i)
        n=sum
    return True
            
            

