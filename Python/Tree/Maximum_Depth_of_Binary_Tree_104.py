#Given a binary tree, find its maximum depth.
class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if not root:return 0
        else:
            left=self.maxDepth(root.left)
            right=self.maxDepth(root.right)
            return max(left,right)+1

    def maxDepth_iterative(self,root):
        if not root: return 0
        cur=root
        stack = [cur]
        count={}
        pre = cur
        count[pre] = 1
        cur=cur.left
        while stack or cur:
            while cur:
                count[cur] = count[pre] + 1
                stack.append(cur)
                pre = cur
                cur=cur.left
            top=stack.pop()
            cur=top.right
            pre=top
        return max(count.values())


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

res=Solution()
print(res.maxDepth_iterative(root))