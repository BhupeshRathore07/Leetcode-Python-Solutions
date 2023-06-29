# You are given an m x n grid grid where:

# '.' is an empty cell.
# '#' is a wall.
# '@' is the starting point.
# Lowercase letters represent keys.
# Uppercase letters represent locks.
# You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

# If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

# For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

# Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

# Example 1:

# Input: grid = ["@.a..","###.#","b.A.B"]
# Output: 8
# Explanation: Note that the goal is to obtain all the keys not to open all the locks.
# Example 2:

# Input: grid = ["@..aA","..B#.","....b"]
# Output: 6
# Example 3:

# Input: grid = ["@Aa"]
# Output: -1
 
# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 30
# grid[i][j] is either an English letter, '.', '#', or '@'.
# The number of keys in the grid is in the range [1, 6].
# Each key in the grid is unique.
# Each key in the grid has a matching lock.








class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m=len(grid)
        n=len(grid[0])
        arr=deque([])
        numOfKeys=0
        keys={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}
        locks={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='@':
                    arr.append((i,j,0,0))
                elif grid[i][j] in keys:
                    numOfKeys+=1

        visited=set()
        while arr:
            size=len(arr)
            for _ in range(size):
                i,j,found,steps=arr.popleft()
                curr=grid[i][j]
                if curr in locks and not (found>>locks[curr]) & 1 or curr=='#':
                    continue

                if curr in keys:
                    found |=1<<keys[curr]
                    if found==(1<<numOfKeys)-1:
                        return steps

                for x,y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if 0<=x<m and 0<=y<n and (x,y,found) not in visited:
                        visited.add((x,y,found))
                        arr.append((x,y,found,steps+1))

        return -1 






