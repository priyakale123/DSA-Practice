arr=[1,2,7,11,15]
target = int(input("Enter target element:"))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            print(i,j)

