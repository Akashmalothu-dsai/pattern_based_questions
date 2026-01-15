nums = [-1,1,0]
count=0
turn=0
while turn<len(nums):
    for i in range(len(nums)-turn):
         num=nums[i:i+turn+1]
         if  sum(num) in nums :
             count+=1
    turn+=1
print(count)
 #-------------------------------
left=0
right=0
sum=0
acount=0
while left<len(nums):
    for right in range(len(nums)):
        sum+=nums[right]
        if sum in nums :
            acount+=1
    left+=1
    
print(acount)
    
    
        
        
