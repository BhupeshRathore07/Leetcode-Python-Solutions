# A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

# Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: s = "1000", k = 10000
# Output: 1
# Explanation: The only possible array is [1000]
# Example 2:

# Input: s = "1000", k = 10
# Output: 0
# Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
# Example 3:

# Input: s = "1317", k = 2000
# Output: 8
# Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only digits and does not contain leading zeros.
# 1 <= k <= 109



class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(str(k))
        dp = [0] * (len(s) + n)

        def get_digit(i):
            return ord(s[i]) - ord('0')

        def get_value(i):
            return get_digit(i)

        if k >= get_value(len(s)-1) and get_value(len(s)-1) != 0:
            dp[len(s)-1] = 1

        for i in reversed(range(0, len(s)-1)):
            if s[i] == '0':
                continue
            for j in range(1+i, min(n+i, len(s))):
                if s[j] == '0':
                    continue
                if k >= int(s[i:j]):
                    dp[i] += dp[j]
                dp[i] %= 1000000007

            if k >= int(s[i:min(n+i, len(s))]):
                if min(n+i, len(s)) == len(s):
                    dp[i] += 1
                else:
                    dp[i] += dp[min(n+i,len(s))]
            dp[i] %= 1000000007

        return dp[0] % 1000000007
