# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        curr=head
        length=0

        while curr:
            length+=1
            curr=curr.next
        
        new=head
        index=0
        to_remove=length-n
        while new:
            if to_remove==0:
                head=new.next
                return head

            if to_remove==index:
                prev_node.next=new.next
                return head
            prev_node=new
            new=new.next
            index+=1



        