# You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

# Example 1:

# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.
# Example 2:

# Input: matrix = [[1,0,1,0,1]]
# Output: 3
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 3.
# Example 3:

# Input: matrix = [[1,1,0],[1,0,1]]
# Output: 2
# Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
 
# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m * n <= 105
# matrix[i][j] is either 0 or 1.









class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        result=0
        max_ones=[0]*len(matrix[0])
        for row in matrix:
            for i, value in enumerate(row):
                max_ones[i]=0 if value==0 else max_ones[i]+1
            sorted_ones=sorted(max_ones)
            for i,h in enumerate(sorted_ones):
                result=max(result,h*(len(row)-i))
        return result






