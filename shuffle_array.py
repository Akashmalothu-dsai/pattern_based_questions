nums = [2,5,1,3,4,7]
k=3
final=[]
for i ,j in zip(nums[:k+1],nums[k:]):
    final+=[i,j]
print(final)
i=0
j=k
#
while i<k:
    final.append(nums[i])
    final.append(nums[j])
    i+=1
    j+=1
print(final)






