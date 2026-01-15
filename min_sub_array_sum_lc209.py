target = 11
nums = [1,1,1,1,1,1,1,1]
left=0
right=0
asum=0
if sum(nums)<target:
    min_length=0
else:
    min_length=len(nums)
while right< len(nums):
    asum+=nums[right]
    if asum>=target:
        while left<=right and sum!=target :
            asum-=nums[left]
            left+=1
        if asum==target:
            length=right-left+1
            if length<min_length:
                min_length=length
                min_sub=nums[left:right+1]
    right+=1
print(min_length)
# optimised solution 
l=0
wind_sum=0
min_len=len(nums)
for r in range(len(nums)):
    wind_sum+=nums[r]
    while wind_sum>=target:
        length=right-left+1
        if min_len>length:
            min_len=length
        wind_sum-=nums[left]
        left+=1

if min_len==len(nums):
    print(f'{0}')
else:
    print(min_len)

    
    
        

       
