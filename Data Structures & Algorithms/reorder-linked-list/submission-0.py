# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # finding the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow

        # Reversing the linked list from the middle
        prev_node = None
        curr = middle.next
        middle.next = None
        while curr:
            temp = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = temp

        s = head
        l = prev_node
        
        while l:
            temp1, temp2 = s.next, l.next
            s.next = l
            l.next = temp1
            s, l = temp1, temp2
        
        
        