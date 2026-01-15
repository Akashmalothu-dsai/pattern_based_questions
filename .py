import numpy as np
def prefixsum(alist):
    prefix_sum=[]
    for i in alist:
        if len(prefix_sum)==0:
            prefix_sum.append(i)
        else:
            prefix_sum.append(i+prefix_sum[-1])
    return prefix_sum
def sum_range(array1,r1,c1,r2,c2):
    arr=np.array(array1)
    sum=0
    for i in range(r1,r2+1):
        prefix_sum_row=prefixsum(arr[0,i,:])
        sum+=prefix_sum_row[c2]-(prefix_sum_row[c1-1] if c1>0 else 0)
    return sum
print(sum_range([[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]],2,1,4,3))
    
    
    