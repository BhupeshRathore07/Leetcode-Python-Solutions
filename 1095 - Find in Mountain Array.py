# (This problem is an interactive problem.)

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

# You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

# Example 1:

# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
# Example 2:

# Input: array = [0,1,2,4,2,1], target = 3
# Output: -1
# Explanation: 3 does not exist in the array, so we return -1.

# Constraints:

# 3 <= mountain_arr.length() <= 104
# 0 <= target <= 109
# 0 <= mountain_arr.get(index) <= 109










class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        # Find the index of the peak element in the mountain array.
        peak_index = self.find_peak_index(1, length - 2, mountain_arr)

        # Binary search for the target in the increasing part of the mountain array.
        increasing_index = self.binary_search(0, peak_index, target, mountain_arr, False)
        if mountain_arr.get(increasing_index) == target:
            return increasing_index  # Target found in the increasing part.

        # Binary search for the target in the decreasing part of the mountain array.
        decreasing_index = self.binary_search(peak_index + 1, length - 1, target, mountain_arr, True)
        if mountain_arr.get(decreasing_index) == target:
            return decreasing_index  # Target found in the decreasing part.

        return -1  # Target not found in the mountain array.

    def find_peak_index(self, low, high, mountainArr):
        while low != high:
            mid = low + (high - low) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1  # Move to the right side (increasing slope).
            else:
                high = mid  # Move to the left side (decreasing slope).
        return low  # Return the index of the peak element.

    def binary_search(self, low, high, target, mountainArr, reversed):
        while low != high:
            mid = low + (high - low) // 2
            if reversed:
                if mountainArr.get(mid) > target:
                    low = mid + 1  # Move to the right side for a decreasing slope.
                else:
                    high = mid  # Move to the left side for an increasing slope.
            else:
                if mountainArr.get(mid) < target:
                    low = mid + 1  # Move to the right side for an increasing slope.
                else:
                    high = mid  # Move to the left side for a decreasing slope.
        return low  # Return the index where the target should be or would be inserted.








