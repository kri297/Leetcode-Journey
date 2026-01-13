# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        while True:
            # Check if there are k nodes remaining
            kth = prev_group
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            # Reverse k nodes
            group_start = prev_group.next
            current = group_start
            prev = None
            for i in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            # Connect with previous group
            prev_group.next = prev
            group_start.next = current
            prev_group = group_start
