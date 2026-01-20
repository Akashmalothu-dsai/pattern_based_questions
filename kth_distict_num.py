alist=[1,2,3,4,1,1]
dis=0
k=int(input("enter the number : "))
for i in alist:
    count=0
    for j in alist:
        if i==j:
            count+=1 
    if count==1:
        dis+=1
        if dis==k:
            print(i)
else:
    print(f"{k} not present this frequency")

# for first_duplicate number 
def first_destict(n):
    f=[]
    for i in n:
        if i in f:
            return i
        f.append(i)
print(first_destict([1,2,2,3,4,4]))


# for the kth distic number 
def kth_distic(n,k):
    count=0
    for i in set(n):
        if n.count(i)==1:
            count+=1
        if count==k:
            return i
print(kth_distic([1,1,2,3,4,5,5],2))
            
        