# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.


# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:

# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 
# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1






class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        num_rows, num_cols = len(grid), len(grid[0])
        
        if grid[0][0] or grid[-1][-1]:
            return -1
        
        if num_rows == 1 and grid[0][0] == 0:
            return 1
        
        queue = collections.deque()
        queue.append((0, 0))
        visited = set()
        visited.add((0, 0))
        step = 1
        
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    
                    if 0 <= new_x < num_rows and 0 <= new_y < num_cols and grid[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        queue.append((new_x, new_y))
                        
                        if new_x == num_rows - 1 and new_y == num_cols - 1:
                            return step + 1
            step += 1
        
        return -1




