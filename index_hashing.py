n=[5,3,2,2,1,5,5,7,5,10]
nums = len(n)
m=[10,111,1,9,5,67,2]
#x= len(m)
hash_dict ={}
for i in range(0,nums):
    hash_dict[n[i]] = hash_dict.get(n[i],0)+1
for i in m:
    if i<1 or i>10:
        print(0)
    else:
        print(hash_dict)    

