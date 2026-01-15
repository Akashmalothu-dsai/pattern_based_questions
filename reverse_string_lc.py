s=["a","K","B"]
left=0
right=len(s)-1
while right>left:
    s[left],s[right]=s[right],s[left]
    left+=1
    right-=1
print(s)