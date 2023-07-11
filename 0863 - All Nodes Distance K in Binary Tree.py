# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
# Example 2:

# Input: root = [1], target = 1, k = 3
# Output: []
 
# Constraints:

# The number of nodes in the tree is in the range [1, 500].
# 0 <= Node.val <= 500
# All the values Node.val are unique.
# target is the value of one of the nodes in the tree.
# 0 <= k <= 1000





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        parent = {}
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for _ in range(size):
                top = queue.popleft()

                if top.left:
                    parent[top.left.val] = top
                    queue.append(top.left)

                if top.right:
                    parent[top.right.val] = top
                    queue.append(top.right)

        visited = {}
        queue.append(target)
        while k > 0 and queue:
            size = len(queue)

            for _ in range(size):
                top = queue.popleft()

                visited[top.val] = 1

                if top.left and top.left.val not in visited:
                    queue.append(top.left)

                if top.right and top.right.val not in visited:
                    queue.append(top.right)

                if top.val in parent and parent[top.val].val not in visited:
                    queue.append(parent[top.val])

            k -= 1

        while queue:
            ans.append(queue.popleft().val)

        return ans



