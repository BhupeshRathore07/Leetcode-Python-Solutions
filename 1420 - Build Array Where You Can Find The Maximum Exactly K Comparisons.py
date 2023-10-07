# You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:


# You should build the array arr which has the following properties:

# arr has exactly n integers.
# 1 <= arr[i] <= m where (0 <= i < n).
# After applying the mentioned algorithm to arr, the value search_cost is equal to k.
# Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.

# Example 1:

# Input: n = 2, m = 3, k = 1
# Output: 6
# Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
# Example 2:

# Input: n = 5, m = 2, k = 3
# Output: 0
# Explanation: There are no possible arrays that satisify the mentioned conditions.
# Example 3:

# Input: n = 9, m = 1, k = 1
# Output: 1
# Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1] 

# Constraints:

# 1 <= n <= 50
# 1 <= m <= 100
# 0 <= k <= n









class Solution:
    def numOfArrays(self, n, m, k):
        if m < k: return 0
        dp = [[1] * m] + [[0] * m for _ in range(k - 1)]
        mod = 10 ** 9 + 7
        for _ in range(n - 1):
            for i in range(k - 1, -1, -1):
                cur = 0
                for j in range(m):
                    dp[i][j] = (dp[i][j] * (j + 1) + cur) % mod
                    if i: cur = (cur + dp[i - 1][j]) % mod
        return sum(dp[-1]) % mod








