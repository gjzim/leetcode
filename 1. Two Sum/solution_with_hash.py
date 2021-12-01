def twoSum(nums, target):
    for i, _ in enumerate(nums):
        for j, _ in enumerate(nums[i+1:]):
            if nums[i]+nums[j+i+1] == target:
                return [i, j+i+1]

    return []

def twoSumHash(nums, target):
    comps = {}
    for i, val in enumerate(nums):
        comp = target-val
        if comp not in comps:
            comps[val] = i
        else:
            return [comps[comp], i]

#print(twoSum([2,7,11,15], 9))
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
print(twoSum([0,-1,1], 0))
