# https://leetcode.com/problems/swap-nodes-in-pairs/
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
        
        return dummy.next

        