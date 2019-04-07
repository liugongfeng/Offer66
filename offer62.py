class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def KthNode(self, root, k):
        self.res = []
        self.mid(root)
        return self.res[k-1] if 0 < k <= len(self.res) else None

    def mid(self, root):
        if not root:  return 
        self.mid(root.left)
        self.res.append(root)
        self.mid(root.right)