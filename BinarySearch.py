arr = [1,3,5,7,9]
target = int(input("Enter target no:"))
left=0
right=len(arr)-1
while left<=right:
    mid = (left+right)//2
    if arr[mid] == target:
        print("Target element is found at index:",mid)
        break 
    elif arr[mid] < target:
        left = mid +1
    else:
        right = mid - 1
else:
    print(" Element not found")            