# Given a string s. In one step you can insert any character at any index of the string.

# Return the minimum number of steps to make s palindrome.

# A Palindrome String is one that reads the same backward as well as forward.

 

# Example 1:

# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we do not need any insertions.
# Example 2:

# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
# Example 3:

# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.


class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        memo = {}

        def dp(i, j):
            if i >= j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i] == s[j]:
                memo[(i, j)] = dp(i+1, j-1)
            else:
                memo[(i, j)] = 1 + min(dp(i+1, j), dp(i, j-1))
            return memo[(i, j)]

        return dp(0, n-1)
