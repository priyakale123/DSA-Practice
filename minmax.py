# Time Complexity: O(n) - ek loop, array chya pratyek element var ekda jato
# Space Complexity: O(1) - फक्त 2 extra variables वापरले

arr=[5,2,9,10,1]
small=arr[0]
largest=arr[0]
for i in arr:
    if i > largest:
        largest= i
    if i < small:
        small=i    
print("largest no is:",largest)  
print("smallest value is:",small)      