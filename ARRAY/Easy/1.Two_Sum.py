nums = [1, 3, 3]
target = 6




for i in range (0, len(nums)-1):
    for j in range (i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print ([i,j])
    


