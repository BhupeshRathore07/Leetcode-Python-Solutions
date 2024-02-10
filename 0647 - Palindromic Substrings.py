# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.












class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total = n

        center = 0.0
        while center < n:
            if center.is_integer():
                left, right = int(center) - 1, int(center) + 1
            else:
                left, right = floor(center), ceil(center)
            
            while left >= 0 and right < n:
                if s[left] != s[right]:
                    break
                total += 1
                left -= 1
                right += 1
            
            center += 0.5
        
        return total

