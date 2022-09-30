# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        try:
            while slow != fast:
                fast = fast.next.next
                slow = slow.next
            return True
        except:
            return False
        
                
        
        
        
        
            
        