nums=[1,0,1,1,0,1]
max_len=0
current_len=0
for i in nums:
    if i==1:
        current_len+=1
    else:
        current_len=0
    if current_len>max_len:
        max_len=current_len
print(max_len)

    


    


    

    

