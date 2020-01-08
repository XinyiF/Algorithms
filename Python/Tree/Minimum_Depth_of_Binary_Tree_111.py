#Given a binary tree, find its minimum depth.
class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        if not root : return 0
        if not root.left and not root.right:return 1
        pre,count,stack,start,res=root,{},[],root,[]
        stack.append(pre)
        count[pre]=1
        cur=root.left
        while stack or cur:
            while cur:
                stack.append(cur)
                count[cur]=count[pre]+1
                pre=cur
                cur=cur.left
            if not pre.right and not pre.left and pre != start:res.append(count[pre])
            top=stack.pop()
            pre=top
            cur=top.right
        return min(res)






#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7
root=TreeNode(1)
root.left=TreeNode(2)


res=Solution()
print(res.minDepth(root))