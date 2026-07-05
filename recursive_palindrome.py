def fun(s,left,right):
    if left>=right:
        return True
    elif s[left] != s[right]:
        return False
    else:
        return fun(s,left+1,right-1)
s= input("Enter String:")
if fun(s,0,len(s)-1):
    print("palindrome")
else:
    print("not palindrome")
        