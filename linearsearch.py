arr = [10,20,1,9]
search = int (input("enter search element :"))
found= False
for i in arr:
    if i== search:
      print("element found:",i)
      found= True
      break
if not found:
   print ("Element not found")   
