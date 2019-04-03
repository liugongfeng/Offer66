class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, tree):
        if not tree:
            return 0
        if not tree.left and not tree.right:
            return 1

        return 1 + max(self.TreeDepth(tree.left), self.TreeDepth(tree.right))
        