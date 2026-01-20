
#brute force
def top_freq(n,k):
    fre={}
    result=[]
    max_count=0
    anum=[[] for _ in range(len(n)+1)]
    for i in n:
        fre[i]=fre.get(i,0)+1
    for num,count in fre.items():
        anum[count].append(num)
    for i in range(len(anum)-1,0,-1):
        if len(anum[i])==0:
            continue
        for j in anum[i]:
            result.append(j)
            if len(result)==k:
                return result
#print(top_freq([1,2,1,2,1,2,3,1,3,2],3))

#optimised
