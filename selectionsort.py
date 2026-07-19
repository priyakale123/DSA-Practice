def selection(nums):
    for i in range(len(nums)):
        min_val = i
        for j in range(i+1,len(nums)):
           if nums[j]<nums[min_val]:
               min_val=j 
        else:nums[i],nums[min_val] = nums[min_val],nums[i]
    print(nums)    
nums =[5,7,8,4,1,6,9]              
selection(nums)
