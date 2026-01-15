array=[1,5,2,4]
tar=0
for i in range(1,len(array)):
    tar^=i
    tar^=array[i]
print(tar)
#xor method is useful when the duplicates are  even other wise there is chance to come different values
