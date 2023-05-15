# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 105
# 0 <= Node.val <= 100



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        
        for i in range(k - 1):
            first = first.next
        
        tmp = first
        second = head
        
        while first.next:
            first = first.next
            second = second.next
        tmp.val, second.val = second.val, tmp.val
        
        return head
