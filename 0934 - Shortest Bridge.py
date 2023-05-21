# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.


# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 1
# Example 2:

# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:

# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
 
# Constraints:

# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] is either 0 or 1.
# There are exactly two islands in grid.






class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]
        island1 = deque()

        def dfs(x, y):
            for dx, dy in directions:
                if 0 <= x + dx < rows and 0 <= y + dy < cols and grid[x + dx][y + dy] == 1:
                    grid[x + dx][y + dy] = 2
                    island1.append([x + dx, y + dy])
                    dfs(x + dx, y + dy)

        def find_island1():
            for x in range(rows):
                for y in range(cols):
                    if grid[x][y]:
                        return dfs(x, y)

        find_island1()
        step = 0
        while island1:
            for _ in range(len(island1)):
                x, y = island1.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 2:
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            island1.append([nx, ny])
                        elif grid[nx][ny] == 1:
                            return step
            step += 1
        return step




