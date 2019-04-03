class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Mirror(self, root):
        if not root:
            return root

        root.left , root.right = root.right, root.left

        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)