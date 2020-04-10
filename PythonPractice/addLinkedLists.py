class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = lSum = ListNode(0)
        carry=0
        while l1 or l2:       
            if l2 is None:
                sum = l1.val + carry
                digit = sum % 10
                carry = sum // 10
                lSum.val = digit
                l1=l1.next
            elif l1 is None:
                sum = l2.val + carry
                digit = sum % 10
                carry = sum // 10
                lSum.val = digit
                l2=l2.next
            else:
                sum = l1.val + l2.val + carry
                digit = sum % 10
                carry = sum // 10
                lSum.val = digit
                l1 = l1.next
                l2 = l2.next
            if l1 or l2 or carry:
                lSum.next = ListNode(0)
                lSum = lSum.next
        return head
        
        