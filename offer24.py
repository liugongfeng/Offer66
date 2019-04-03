class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def FindPath(self, root, num):
        if not root:
            return []
        
        if not root.left and not root.right and num == root.val:
            return [[root.val]]
        
        res = []
        left = self.FindPath(root.left, num - root.val)
        right = self.FindPath(root.right, num - root.val)

        for i in left + right:
            res.append([root.val] + i)
        return res
