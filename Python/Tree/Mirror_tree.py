#mirror of a tree
class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def Mirror(self, root):
        if not root: return root
        temp= root.left
        root.left=root.right
        root.right=temp
        self.Mirror(root.left)
        self.Mirror(root.right)








