# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr is None:
            return curr
        prev_node = None

        while curr:
            new = ListNode(curr.val)
            new.next = prev_node
            prev_node = new
            curr = curr.next
        return prev_node