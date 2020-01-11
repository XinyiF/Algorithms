#determine if Tree B is subtree of Tree A
class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:return False
        res1=self.preorderTraversal(pRoot1)
        res2 =self.preorderTraversal(pRoot2)
        for i in res2:
            if not i in res1:
                return False
            elif res2[i].left and not res1[i].left or res2[i].left and res2[i].left.val != res1[i].left.val:
                return False
            elif res2[i].right and not res1[i].right or res2[i].right and res2[i].right.val != res1[i].right.val:
                return False
        return True

    def preorderTraversal(self, root):
        res = {}  # store result
        stack = []  # helper stack
        cur = root  # current node
        while stack or cur:
            while cur:
                res[cur.val]=cur
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            cur = top.right
        return res








#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)

tree=TreeNode(2)
tree.left=TreeNode(4)
tree.right=TreeNode(5)

res=Solution()
print(res.HasSubtree(root,tree))