#Enter an integer array to determine whether the array is the result
# of a post-order traversal of a binary search tree
class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:return False
        for i in range(len(sequence)):
            if sequence[i]>=sequence[len(sequence)-1]:
                i-=1
                break
        left=sequence[:i+1]
        right=sequence[i+1:len(sequence)-1]
        for j in right:
            if j<sequence[-1]:
                return False
        self.VerifySquenceOfBST(left)
        self.VerifySquenceOfBST(right)
        return True


s=[1,2,3,4,5]
res=Solution()
print(res.VerifySquenceOfBST(s))