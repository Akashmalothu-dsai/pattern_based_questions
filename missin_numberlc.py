n=[1,2,4,4]
total_sum=((len(n)+1)*len(n))/2
number=[]
k=0
while k<len(n):
    if n[k] in number:
        duplicate=n[k]
    number.append(n[k])
    k+=1
print([duplicate,int(total_sum-sum(n)+duplicate)])





    


