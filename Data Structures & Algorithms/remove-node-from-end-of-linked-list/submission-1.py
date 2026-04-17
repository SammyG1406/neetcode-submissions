# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # if n is equal to the length, that means remove the first element of the list
        if length == n:
            return head.next
        
        prev_node, start = None, head
        c = 1
        while start:
            if c == (length + 1) - n:
                prev_node.next = start.next
                start.next = None
                return head
            c += 1
            prev_node = start
            start = start.next