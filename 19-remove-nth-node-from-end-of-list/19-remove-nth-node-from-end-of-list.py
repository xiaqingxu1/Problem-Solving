# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return
        
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        
        if l == n:
            head = head.next
            
        
        else:
            step = l - n - 1 
            cur = head
            while step > 0:
                cur = cur.next
                step -= 1
            temp = cur.next
            cur.next = temp.next
        
        return head
        
        
        
        
            
        