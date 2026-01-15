

#-------MAX_WATER STORE---- 
n=[1,8,6,2,5,4,8,3,7]
left=0
right=len(n)-1
max_area=0
while left<right:
    if n[left]<n[right]:
        area=n[left]*(right-left)
        left+=1
    else:
        area=n[right]*(right-left)
        right-=1
    if area>max_area:
        max_area=area

print(max_area)
#out put will be the max_area(quantity of the water)

#same problem with different out put 
n=[1,8,6,2,5,4,8,3,7]#height's
left=0
right=len(n)-1
max_area=0
while left<right:
    if n[left]>n[right]:
        area=n[right]*(right-left)
        right-=1
    else:
        area=n[left]*(right-left)
        left+=1
        
    if area>max_area:
        max_area=area
        index=[left,right]
print(index)#line of the height for which cause to max_area of store's
