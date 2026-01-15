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