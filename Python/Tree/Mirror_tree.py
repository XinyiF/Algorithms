#mirror of a tree
class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def Mirror_recursive(self, root):
        if not root: return root
        temp= root.left
        root.left=root.right
        root.right=temp
        self.Mirror(root.left)
        self.Mirror(root.right)

    def Mirror(self,root):
        if not root: return root
        cur,stack=root,[]
        while stack or cur:
            while cur:
                temp=cur.left
                cur.left=cur.right
                cur.right=temp
                stack.append(cur)
                cur=cur.left
            top=stack.pop()
            cur =top.right
        return root








