def contiguous_array(nums):#this is not more effective and tle will raise
    max_len=0
    for left in range(len(nums)):
        sum=0
        for right in range(left,len(nums)):
            sum+=nums[right]
            if 2*sum==(right-left+1) and max_len<2*sum:
                max_len=right-left+1
    return max_len
print(contiguous_array([0,1,1,1,1,1,0,0,0]))

#other method (optimised approach)
def second_method(nums):
    prefix=0
    max_len=0
    prefix_index={0:-1}
    for right in range(len(nums)):
        if nums[right]==0:
            prefix-=1
        else:
            prefix+=1
        if prefix in prefix_index:
            max_len=max(max_len,right-prefix_index[prefix])
        else:
            prefix_index[prefix]=right
    return max_len

print(second_method([0,1,1,1,1,1,0,0,0]))