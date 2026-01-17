
#brute force logic 
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

#optimised _way (time efficiect)
def prefix_2d_sum(n):
    rows=len(n)
    coloums=len(n[0])
    prefix_matrix=[[0]*coloums for _ in range(rows)]
    for i in range(rows):
        for j in range(coloums):
            top=prefix_matrix[i-1][j] if i>0 else 0
            left=prefix_matrix[i][j-1] if j>0 else 0
            top_left=prefix_matrix[i-1][j-1] if i>0 and j>0 else 0
            prefix_matrix[i][j]=n[i][j]+top+left-top_left
    return prefix_matrix


def sum_range(r1,c1,r2,c2):
    top=prefix_sum[r1-1][c2] if r1>0 else 0
    left=prefix_sum[r2][c1-1] if c1>0 else 0
    top_left=prefix_sum[r1-1][c1-1] if r1>0 else 0
    total=prefix_sum[r2][c2]
    return total-top-left+top_left
prefix_sum=prefix_2d_sum([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(sum_range(2,1,4,3))