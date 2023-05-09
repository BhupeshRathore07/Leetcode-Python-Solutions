# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
  
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100



class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        
        res = []
        i_min = 1
        j_min = 0
        i_max = len(matrix)-1
        j_max = len(matrix[0])-1
        
        direction = "R"
        i = j = 0
        
        for k in xrange((i_max+1)*(j_max+1)):
            res.append(matrix[i][j])
            if direction == "R":
                if j+1 > j_max:
                    direction = "D"
                    j_max-=1
                    i+=1
                else:
                    j+=1
            elif direction == "D":
                if i+1 > i_max:
                    direction = "L"
                    i_max-=1
                    j-=1
                else:
                    i+=1
            elif direction == "L":
                if j-1 < j_min:
                    direction = "U"
                    j_min+=1
                    i-=1
                else:
                    j-=1
            else: # direction == "U"
                if i-1 < i_min:
                    direction = "R"
                    i_min+=1
                    j+=1
                else:
                    i-=1
        
        return res


