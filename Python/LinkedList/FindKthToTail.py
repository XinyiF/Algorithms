#Enter a linked list and output the k-th node from the bottom of the linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head:return None
        count,index={},0
        while head:
            index += 1
            count[index]=head
            head=head.next
        if k>index or k==0:return None
        return count[index-k+1]
