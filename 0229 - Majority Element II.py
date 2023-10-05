# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109

# Follow up: Could you solve the problem in linear time and in O(1) space?







class Solution:
    def majorityElement(self, nums):

        count_dict = Counter(nums)
        result = [num for num, count in count_dict.items() if count > len(nums) // 3]
        return result





