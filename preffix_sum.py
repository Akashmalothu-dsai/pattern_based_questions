def prefix_sum(nums:list):
    res=[]
    for i in range(len(nums)):
        n=nums[i]
        if len(res)==0:
            res.append(n)
        else:
            res.append(n+res[i-1])
    return res
print(prefix_sum([1,2,3,4]))         
def sum_range(nums,left,right):
    return prefix_sum(nums)[right]-(prefix_sum(nums)[left-1] if left >0  else 0)
print(sum_range([1,2,3,4],0,3))