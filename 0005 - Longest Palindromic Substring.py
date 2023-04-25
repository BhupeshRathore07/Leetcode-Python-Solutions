# Given a string s, return the longest palindromic substring in s.

#  Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
    
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        for i in range(len(s)):
            palindrome1 = expand_around_center(s, i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1
                
            palindrome2 = expand_around_center(s, i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2
                    
        return longest
