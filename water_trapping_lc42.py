h = [0,1,0,2,1,0,1,3,2,1,2,1]
left=0
right=len(h)-1
max_left=0
max_right=0
water=0
while right>left:
    if h[left]<h[right]:
        if h[left]>=max_left:
            max_left=h[left]
        else:
            water+=max_left-h[left]
        left+=1
    else:
        if h[right]>=max_right:
            max_right=h[right]
        else:
            water+=max_right-h[right]
        right-=1
print(water)
