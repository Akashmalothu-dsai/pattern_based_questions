#with sorted and brute force 
nums = [1,0,1,2]
nums=sorted(set(nums))
count=0
max_count=0
for i in range(1,len(nums)):
    if nums[i]-nums[i-1]==1:
        count+=1
    else:
        max_count=count
print(max_count+1)
#optimised 
def consective_sequence(n):
    n=set(n)
    max_count=0
    for i in n:
        if i-1 not in n:
            current=i
            count=1
            while current+1 in n:
                current+=1
                count+=1
            if max_count<count:
                max_count=count
        # if max_count<count: this can also give the same solution
        #        max_count=count  
    return max_count
print(consective_sequence([1,0,1,2,5,6,7,8,9,10]))
                
        
