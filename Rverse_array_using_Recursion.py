def swap(nums,L,R):
    if L>=R:
        return nums
        
    else:
        nums[L],nums[R] = nums[R],nums[L]
        return swap(nums,L+1,R-1)
num = [5,9,8,3,6,7,1,4,2]
l=0
r=len(num)-1
print(swap(num,l,r))        