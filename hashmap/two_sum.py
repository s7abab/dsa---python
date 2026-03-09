def twoSum(nums,target):
    hash= {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in hash:
            return [hash[complement], i]
        
        hash[num] = i

# 2+1 = 3
nums = [2,1,4,5]

print(twoSum(nums, 3))