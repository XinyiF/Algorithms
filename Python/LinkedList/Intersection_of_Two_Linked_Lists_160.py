#Write a program to find the node at which the intersection of two singly linked lists begins.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        temp = {}
        while headA:
            temp[headA] = 1
            headA = headA.next
        while headB:
            if headB in temp:
                return headB
            headB=headB.next
        return None


l0 = ListNode(3)
l1 = ListNode(2)
l2 = ListNode(2)
l3 = ListNode(4)
l4 = ListNode(6)

l0.next = l1
l1.next = l2
l2.next = None
l4.next = l3
l3.next = l2

headA = l0
headB = l4

res = Solution()
resu = res.getIntersectionNode(headA, headB)
print(resu)
