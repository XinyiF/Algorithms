class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        prev=ListNode(-1)
        head=prev
        while l1 and l2:
            if l1.val<=l2.val:
                head.next=l1
                l1=l1.next
            else:
                head.next=l2
                l2=l2.next
            head=head.next
        if not l1 and l2:
            head.next=l2
        if l1 and not l2:
            head.next=l1
        return prev.next
