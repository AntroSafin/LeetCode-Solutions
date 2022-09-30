# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        temp = ListNode()
        list3 = temp
        while(l1 or l2):
            value = 0
            if(l1):
                value += l1.val
                l1 = l1.next
            if(l2):
                value += l2.val
                l2 = l2.next
            value += carry
            if(value>9):
                value = value%10
                carry = 1
            else:
                carry = 0
            list3.next = ListNode(value)
            list3 = list3.next
        if(carry):
            list3.next = ListNode(carry)
        return temp.next
