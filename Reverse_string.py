def reverse(s):
    char = list(s)
    left=0
    right = len(char)-1
    while left<right:
        char[left],char[right] = char[right],char[left]
        left+=1
        right-=1
    return "".join(char)
   
s = input("Enter string:")
print("Reversed string:",reverse(s))    
    