class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

tree=TreeNode('A')
tree.val=1
tree.left=TreeNode('B')
tree.left.val=2
print(tree)
