# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        def findMid(head):
            a, b = head, head
            while b.next and b.next.next:
                a = a.next
                b = b.next.next
            mid = a.next
            a.next = None
            return head, mid
        
        def reverse(head):
            a, b, c = None, head, head.next
            while b and b.next:
                b.next = a
                a = b
                b = c
                c = b.next
            b.next = a
            return b
        
        head1, head2 = findMid(head)
        head2 = reverse(head2)
        
        while head1 and head2:
            next1, next2 = head1.next, head2.next
            head1.next = head2
            head2.next = next1
            head1, head2 = next1, next2
        return head
        
        
        