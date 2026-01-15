
#BRUTE METHOD (WHICH IS NOT OPTIMISED )

a = "ADOBECODEBANC"
t = "ABC"
k=len(t)
min=len(a)
while k<=len(a):
    for i in range(len(a)):
        sub=a[i:i+k]
        sub_list=list(sub)
        for  i in t:
            if i not in  sub_list:
                break 
            else:
                sub_list.remove(i)
        else:
            if min>len(sub):
                min=len(sub)
                min_sub=sub
            
    k+=1

# WITH OPTIMISED
from collections import Counter


#counter is the liberary which make the directly converts the dic map the elements to frequency
s = "AA"
t = "AA"
need=Counter(t)
window={}
required=len(need)
formed=0
left=0
start=0
min_sub=""
min_len=len(s)
for right in range(len(s)):
    chr=s[right]
    window[chr]=window.get(chr,0)+1
    if chr in need and window[chr]==need[chr]:
        formed+=1
    while formed==required:
        length =right-left+1
        if min_len>=length:
            min_len=length
            min_sub=s[left:right+1]
        left_chr=s[left]
        window[left_chr]-=1
        if left_chr in need and window[left_chr]<need[left_chr]:
            formed-=1
        left+=1
print(min_sub)

        

    










           