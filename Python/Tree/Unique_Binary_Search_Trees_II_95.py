class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        if n < 1: return []
        def generate_trees(start, end):
            if start > end:
                return [None]
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)

            return all_trees

        return generate_trees(1, n)


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
print(res.generateTrees(3))





