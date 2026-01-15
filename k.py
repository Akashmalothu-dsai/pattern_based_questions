alist=[2,3,4]
target=6
for i in range(len(alist)):
    remain=target-alist[i]
    if remain in alist and alist.index(remain)!=i:
        index=[i,alist.index(remain)]
        print(index)
        break