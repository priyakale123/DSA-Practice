str= input("enter string:").lower()
n= len(str)
left=0
right= n-1
while left<=right:
    print(left,right,str[left],str[right])
    if str[left] != str[right]:
      print("not palindrome")
      break
    left += 1
    right -= 1
else:
   print("string is palindrome")
   
       