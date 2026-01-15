n="abcabdcdccdxw"
count=0
left=0
seen=set()
for right in range(len(n)):
    while n[right] in seen:
        seen.remove(n[left])
        left+=1
    seen.add(n[right])
    if right-left+1>count:
        count=right-left+1
        max_sub=n[left:right+1]
print(max_sub)



            
        























