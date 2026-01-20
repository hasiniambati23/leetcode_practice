nums=[1,1,2]
if not nums:  
    print(0) 

    j = 0  
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1 
            nums[j] = nums[i] 
    print(j + 1) 