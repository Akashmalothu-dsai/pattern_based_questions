#brute force
n=["eat","tea","tan","ate","nat","bat"]
total=[]
result=[]

for i in n:
    a=[]
    if set(i) not in total:
        total.append(set(i))
        for j in n:
            if sorted(i)==sorted(j):
                a.append(j)
        result.append(a)    
print(result)
#<<<<---optimised--->>>>#
def analgram(n):
    anagram={}
    for i in n:
        key=tuple(sorted(i))
        if  key in anagram:
            anagram[key].append(i)
        else:
            anagram[key]=[i]
    return list(anagram.values())
print(analgram(n))