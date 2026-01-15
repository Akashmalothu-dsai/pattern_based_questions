
#two pointer form 
def palindrome(n):
    left=0
    right=len(n)-1
    while left<right:
        if n[left]!=n[right]:
            return False
        left+=1
        right-=1
    else:
        return True
n="malothu akash"
print(n.split(","))
#-------2 methood -----------------
def polindrome(n):
    if n[::-1]==n:
        return True
    else:
        return False


