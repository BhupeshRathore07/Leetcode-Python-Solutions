# Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

# Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

# A full binary tree is a binary tree where each node has exactly 0 or 2 children.

# Example 1:

# Input: n = 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Example 2:

# Input: n = 3
# Output: [[0,0,0]]

# Constraints:

# 1 <= n <= 20








# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        memo = {}

        def _allPossibleFBT(n):
            if n in memo:
                return memo[n]

            list = []
            if n == 1:
                list.append(TreeNode(0))
            else:
                for i in range(1, n - 1, 2):
                    lTrees = _allPossibleFBT(i)
                    rTrees = _allPossibleFBT(n - i - 1)

                    for lt in lTrees:
                        for rt in rTrees:
                            list.append(TreeNode(0, lt, rt))

            memo[n] = list
            return list

        return _allPossibleFBT(n)


