class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        n = len(nums) 

        for i in range(0, n):
            remain = target - nums[i]
            if remain in hash_map:
                return [hash_map[remain], i]

            hash_map[nums[i]] = i
        