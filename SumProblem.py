arr = [2, 7, 11, 15]

target = int(input("Enter target: "))

left = 0
right = len(arr) - 1

while left < right:

    current_sum = arr[left] + arr[right]

    if current_sum == target:
        print("Indices:", left, right)
        print("Values:", arr[left], arr[right])
        break

    elif current_sum > target:
        right -= 1

    else:
        left += 1