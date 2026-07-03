arr=[5,8,1,9,2,4]
n=len(arr)
print("Array before sort",arr)
swap = False
for i in range(n-1):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
        swap = True
        if swap == False:
            break
print("sorted array is:",arr)        


    