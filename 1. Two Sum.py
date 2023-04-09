class Solution(object):
    def twoSum(self, nums, target):
        ans = {}
        for i in range(len(nums)):
            if target - nums[i] in ans:
                return [ans[target-nums[i]], i]
            
            else:
                ans[nums[i]] = i
