# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
# the smallest in lexicographical order among all possible results.

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.
 
# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/








class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n=len(s)
        lookup={}
        for i in range(n):
            lookup[s[i]]=i
        ans=[]
        for i in range(n):
            if s[i] not in ans:
                while ans and ans[-1]>s[i] and lookup[ans[-1]]>i:
                    ans.pop()
                ans.append(s[i])
        return "".join(ans)                





