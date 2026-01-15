#optimised one way 

from collections import Counter
s1 = "ab"
s2="abur"
window={}
need=Counter(s1)
required=len(need)
left=0
match=0
f=False
for right in range(len(s2)):
    chr=s2[right]
    window[chr]=window.get(chr,0)+1
    if chr in need and window[chr]==need[chr]:
        match+=1
    f=False
    while match==required:
        if len(s1)==len(s2[left:right+1]):
            f=True
        left_chr=s2[left]
        window[left_chr]-=1
        if left_chr in need and window[left_chr]<need[left_chr]:
            match-=1
        left+=1
    if f==True :
        print(True)
        break

if f==False:
    print(False)
#optimised 
require=len(needed)
match=0
awindow={}
for right in range(len(s2)):
    chr=s2[right]
    awindow[chr]=awindow.get(chr,0)+1
    if chr in needed and needed[chr]==awindow[chr]:
        match+=1
    while right-left+1>len(s1):
        left_chr=s2[left]
        awindow[chr]-=1
        if left_chr in needed and awindow[left_chr]<needed[left_chr]:
            match-=1
        left+=1
    if match==require:
        print(True)
        break
    else:
        print(False)
        break


   

        
    
    

            

       






