
s = "cbaebabacd"
p = "abc"
window={}
need={}
for i in p:
    if i in need:
        need[i]+=1
    else:
        need[i]=1
require=len(need)
left=0
index=[]
for right in range(len(s)):
    chr=s[right]
    window[chr]=window.get(chr,0)+1
    if chr in need and need[chr]==window[chr]:
        require-=1
    while require==0:
        if len(p)==len(s[left:right+1]):
            index.append(left)
        left_chr=s[left]
        window[left_chr]-=1
        if left_chr in need and need[left_chr]>window[left_chr]:
            require+=1
        left+=1
print(index)


    





    