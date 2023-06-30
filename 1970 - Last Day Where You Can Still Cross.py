# There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

# Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

# You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

# Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

# Example 1:

# Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
# Output: 2
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 2.
# Example 2:

# Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
# Output: 1
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 1.
# Example 3:

# Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
# Output: 3
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 3.

# Constraints:

# 2 <= row, col <= 2 * 104
# 4 <= row * col <= 2 * 104
# cells.length == row * col
# 1 <= ri <= row
# 1 <= ci <= col
# All the values of cells are unique.







class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row * col
        root, left, right = list(range(n)), [0] * n, [0] * n 
        for i in range(col):
            for j in range(row):
                left[i * row + j] = i
                right[i * row + j] = i
                
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        def union(x, y):
            a, b = find(x), find(y)
            if a != b:
                root[a] = b
            left[b] = min(left[b], left[a]) 
            right[b] = max(right[b], right[a])
            
        seen = set()
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
        for i, cell in enumerate(cells):
            cx, cy = cell[0] - 1, cell[1] - 1
            for dx, dy in dirs:
                x, y = cx + dx, cy + dy
                if 0 <= x < row and 0 <= y < col and (x, y) in seen:
                    union(cy * row + cx, y * row + x)
                    new = find(y * row + x)
                    if left[new] == 0 and right[new] == col - 1:
                        return i
            seen.add((cx, cy))
        return n




