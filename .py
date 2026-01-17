nums = [4,5,0,-2,-3,1]
k = 5
count=0
seen={0:1}
prefix_sum=0
for i  in nums:
    prefix_sum+=i
    rem=prefix_sum%k
    if rem in seen:
        count+=seen[rem]
    seen[rem]=seen.get(rem,0)+1#for every sum we are madeed require 
print(count) 
    