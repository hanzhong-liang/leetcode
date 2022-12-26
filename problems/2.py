# time O(n) space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         l1_head = l1
#         l2_head = l2
#         l1_l2 = 0
#         carry = 0
#         while l1 and l2:
#             two_sum = l1.val+l2.val+carry
#             if two_sum>=10:
#                 two_sum=two_sum%10
#                 carry=1
#             else:
#                 carry=0
#             l1.val=two_sum
#             l2.val=two_sum
#             l1 = l1.next
#             l2 = l2.next
        
#         while l1:
#             l1_l2 = 0
#             two_sum = l1.val+carry
#             if two_sum>=10:
#                 two_sum=two_sum%10
#                 carry=1
#             else:
#                 carry=0
#             l1.val=two_sum
#             l1 = l1.next
            
#         while l2:
#             l1_l2 = 1
#             two_sum = l2.val+carry
#             if two_sum>=10:
#                 two_sum=two_sum%10
#                 carry=1
#             else:
#                 carry=0
#             l2.val=two_sum
#             l2 = l2.next
        
#         if carry:
#             if l1_l2:
#                 l2 = l2_head
#                 while l2.next:
#                     l2 = l2.next
#                 l2.next = ListNode(val=1)
#             else:
#                 l1 = l1_head
#                 while l1.next:
#                     l1 = l1.next
#                 l1.next = ListNode(val=1)
                
#         return l2_head if l1_l2 else l1_head
        
        dummy_head = ListNode(val=-1)
        cur = dummy_head
        carry = 0
        while l1 or l2 or carry:
            two_sum = (l1.val if l1 else 0)+(l2.val if l2 else 0)+carry
            if two_sum>=10:
                two_sum=two_sum%10
                carry=1
            else:
                carry=0
            cur.next = ListNode(val=two_sum)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next