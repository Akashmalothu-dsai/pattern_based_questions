nums = [1,1,1]
k = 2
count=0
seen={0:1}
prefix_sum=0
for i in nums:
    prefix_sum+=i
    if prefix_sum-k in seen:
        count+=seen[prefix_sum-k]
    seen[prefix_sum]=seen.get(prefix_sum,0)+1
print(count)


#---------------------------------#brute force method---------
def prefix_sum(n):
    alist=[]
    prefix_sum=0
    for i in n:
        prefix_sum+=i
        alist.append(prefix_sum)
    return alist

def max_sum(n,k):
    sum=prefix_sum(n)
    count=0
    seen={0:1}#this function similarly two sum if they are not sorted manner 
    for i in sum:
        required=i-k 
        if required in seen:
            count+=seen[required]
        seen[i]=seen.get(i,0)+1
    return count
print(max_sum([1,1,1],2))
        
        
    

    
        