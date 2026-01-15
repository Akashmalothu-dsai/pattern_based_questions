alist=[1,2,3,4,6]
target=int(input("enter target"))
for i in range(len(alist)):
    for j in range(len(alist)):
        if i==j:
            continue
        sum=alist[i]+alist[j]
        if sum==target:
            index=[i,j]
            print(index)


#-----------optimised----------------
def twoSum( nums, target: int):
    for i in range(len(nums)):
        remain=target-nums[i]
        if remain in nums and nums.index(remain)!=i:
            index=[i,nums.index(remain)]
            return index
print(twoSum([1,2,4],3))


#----other method--------------
def twosum(nums,target):
    seen={}
    for i in range(len(nums)):
        remain=target-nums[i]
        if remain in seen:
            return f'{[seen[remain],i]}'
        seen[nums[i]]=i
   
