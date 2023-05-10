# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

# Example 1:

# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 20



class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
    
        # Define the boundaries of the matrix
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        
        # Define the current value to be filled in the matrix
        num = 1
        
        while top <= bottom and left <= right:
            # Fill the top row
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            
            # Fill the right column
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            # Fill the bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1
            
            # Fill the left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        
        return matrix


