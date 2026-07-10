nums=[5,6,7,7,1,9,111,1,1,5,1,1]
frequen_map = {}
for i in range(0,len(nums)):
    if nums[i] in frequen_map:
        frequen_map[nums[i]] +=1
    else:
        frequen_map[nums[i]] = 1
    print(frequen_map)      