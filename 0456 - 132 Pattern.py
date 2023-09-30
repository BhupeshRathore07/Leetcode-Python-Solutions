# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
# Example 2:

# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# Example 3:

# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

# Constraints:

# n == nums.length
# 1 <= n <= 2 * 105
# -109 <= nums[i] <= 109







class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)

        if length < 3:
            return False

        decreasing_stack = deque()
        max_third_element = float('-inf')

        for i in range(length - 1, -1, -1):
            current_number = nums[i]

            if current_number < max_third_element:
                return True 

            while decreasing_stack and decreasing_stack[0] < current_number:
                max_third_element = decreasing_stack.popleft()

            decreasing_stack.appendleft(current_number)

        return False








