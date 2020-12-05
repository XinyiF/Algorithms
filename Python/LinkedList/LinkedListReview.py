class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def deleteDuplicates(self, head):
        """
        1->1->1->2->3
        1->2->3
        :param head:
        :return: 去掉重复部分
        """
        if not head:
            return head
        node,val=[],[]
        while head:
            if head.val not in val:
                node.append(head)
                val.append(head.val)
            head=head.next
        start,head=node[0],node[0]
        for h in node[1:]:
            head.next=h
            head=head.next
        head.next=None
        return start

    def deleteDuplicates2(self, head):
        """
        1->1->1->2->3
        2->3
        :param head:
        :return: 去掉所有有重复val的node
        """
        if not head:
            return head
        record={}
        while head:
            if not head.val in record:
                record[head.val]=[head]
            else:
                record[head.val].append(head)
            head=head.next
        newhead=ListNode(-1)
        start=newhead
        for val in record:
            if len(record[val])==1:
                newhead.next=record[val][0]
                newhead=newhead.next
        newhead.next=None
        return start.next

    def reverseList(self, head):
        """
        反转链表
        :param head:
        :return:
        """
        if not head:
            return head
        dummy=None
        pre=dummy
        while head:
            nex=head.next
            head.next=pre
            pre=head
            head=nex
        return pre

    def reverseBetween(self, head, m, n):
        """
        扫描一遍反转位置m～n
        :param head:
        :param m:
        :param n:
        :return:
        """
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        pre, nex = None, None
        for i in range(m):
            pre = head
            # head指向m位置
            head = head.next
            nex = head.next
        # 第一段尾部
        head1 = pre
        # 第二段反转前头部
        head2 = head
        for i in range(m, n + 1):
            nex = head.next
            head.next = pre
            pre = head
            # 最后head指向n+1位置
            head = nex
        # 第二段反转前尾部
        tail2 = pre
        head3 = head
        head1.next = tail2
        head2.next = head3
        return dummy.next

    def mergeTwoLists(self, l1, l2):
        """
        将两个升序链表合并为一个新的升序链表并返回
        做一个dummy一个一个加上去就行
        :param l1:
        :param l2:
        :return:
        """
        dummy=ListNode(-1)
        start=dummy
        while l1 and l2:
            if l1.val<l2.val:
                dummy.next=ListNode(l1.val)
                l1=l1.next
            else:
                dummy.next=ListNode(l2.val)
                l2=l2.next
            dummy=dummy.next
        if not l1:
            dummy.next=l2
        else:
            dummy.next=l1
        return start.next

    def partition(self, head, x):
        """
        给定一个链表和一个特定值 x，对链表进行分隔，
        使得所有小于 x 的节点都在大于或等于 x 的节点之前
        :param head:
        :param x:
        :return:
        """
        dummy1=ListNode(-1)
        start1=dummy1
        dummy2=ListNode(-1)
        start2=dummy2
        while head:
            if head.val>=x:
                dummy1.next=ListNode(head.val)
                dummy1=dummy1.next
            else:
                dummy2.next=ListNode(head.val)
                dummy2=dummy2.next
            head=head.next
        dummy2.next=start1.next
        dummy1.next=None
        return start2.next

    def reorderList(self, head):
        """
        快慢指针找断点，断成两个链表
        后一个链表反转
        交叉连接
        :param head:
        :return:
        """
        if not head or not head.next or not head.next.next:
            return head
        faster=head
        slower=head
        while faster and faster.next:
            faster=faster.next.next
            slower=slower.next
        newHead=slower.next
        slower.next=None
        # 两个新链表 head，newHead
        # 反转newHead
        dummy=ListNode(-1)
        dummy.next=newHead
        pre=dummy
        cur=newHead
        while cur:
            nex=cur.next
            cur.next=pre
            pre=cur
            cur=nex
        # pre是目前的head
        newHead.next=None
        # 新链表head，pre
        root=head
        dummy=ListNode(-1)
        while head and pre:
            dummy.next=head
            dummy=dummy.next
            head=head.next
            dummy.next=pre
            dummy=dummy.next
            pre=pre.next
        if not head:
            dummy.next=pre
        if not pre:
            dummy.next=head
        return root

    def hasCycle(self, head):
        """
        快慢指针相遇则有环
        :param head:
        :return:
        """
        faster,slower=head,head
        while faster and faster.next:
            slower=slower.next
            faster=faster.next.next
            if slower==faster:
                return True
        return False

    def isPalindrome(self, head):
        """
        判断回文链表
        :param head:
        :return:
        """
        if not head:
            return True
        faster,slower,pre=head,head,head
        while faster and faster.next:
            faster=faster.next.next
            pre=slower
            slower=slower.next
        # 断开,slower,head
        pre.next=None
        head1,head2=head,slower
        # 反转head2;
        dummy=ListNode(-1)
        dummy.next=head2
        pre=dummy
        cur=head2
        while cur:
            nex=cur.next
            cur.next=pre
            pre=cur
            cur=nex
        head2.next=None
        head3=pre
        # 比较head1，head3
        while head1 and head3:
            if head1.val!=head3.val:
                return False
            head1=head1.next
            head3=head3.next
        return True




















