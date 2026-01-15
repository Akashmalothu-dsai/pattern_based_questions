nums = [-1,0,1,2,-1,-4]
nums.sort()
n=len(nums)
result=[]
for i in range(n-2):
    if i>0 and nums[i-1]==nums[i]:
        continue
    left=i+1
    right=n-1
    while left<right:
        sum=nums[left]+nums[right]+nums[i]
        if sum==0:
            result.append([nums[i],nums[left],nums[right]])
            right-=1
            left+=1
            while right>left and nums[left]==nums[left-1]:
                 left+=1
            while right>left and nums[right]==nums[right+1]:
                 right-=1
            
        elif sum>0:
             right-=1
        else:
             left+=1
print(result)
            
            
    
    
        
