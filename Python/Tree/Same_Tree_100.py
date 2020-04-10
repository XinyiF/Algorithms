#Given two binary trees, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif p !=None and q!=None:
            if p.val==q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            else:return False
        else:return False

p=TreeNode('A')
p.val=1
p.left=TreeNode('B')
p.left.val=2
p.right=TreeNode('C')
p.right.val=None

q=TreeNode('A')
q.val=1
q.left=TreeNode('B')
q.left.val=2
q.right=TreeNode('C')
q.right.val=1

res=Solution()
print(res.isSameTree(p,q))
