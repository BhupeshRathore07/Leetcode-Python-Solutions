# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]

# Constraints:

# 1 <= numRows <= 30





class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = [(row:= [1])]

        for _ in range(1, numRows):

            row = list(map(sum,pairwise([0]+row+[0])))
            ans.append(row)

        return ans




